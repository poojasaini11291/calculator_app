from decimal import Decimal

import pytest


@pytest.mark.parametrize(
    ("first_number", "second_number", "operation", "expected"),
    [
        ("10", "5", "addition", "15"),
        ("10", "5", "subtraction", "5"),
        ("10", "5", "multiplication", "50"),
        ("10", "5", "division", "2"),
        ("2.5", "1.5", "addition", "4"),
    ],
)
def test_calculate_operations(
    client,
    first_number: str,
    second_number: str,
    operation: str,
    expected: str,
):
    response = client.post(
        "/calculate",
        json={
            "first_number": first_number,
            "second_number": second_number,
            "operation": operation,
        },
    )

    assert response.status_code == 200
    assert Decimal(response.json()["result"]) == Decimal(expected)


def test_division_by_zero_is_rejected(client):
    response = client.post(
        "/calculate",
        json={
            "first_number": "10",
            "second_number": "0",
            "operation": "division",
        },
    )

    assert response.status_code == 422


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("25", "5"),
        ("20.25", "4.5"),
        ("0", "0"),
        ("2", "1.41421356"),
    ],
)
def test_square_root(value: str, expected: str, client):
    response = client.post("/sqrt", json={"value": value})

    assert response.status_code == 200
    assert response.json()["result"] == expected


def test_square_root_of_negative_returns_exact_error(client):
    response = client.post("/sqrt", json={"value": "-1"})

    assert response.status_code == 422
    assert response.json()["detail"] == (
        "Invalid input. Square root of a negative number is not supported."
    )


def test_square_root_rounds_half_up_to_eight_decimal_places(client):
    response = client.post("/sqrt", json={"value": "1.000000010000000025"})

    assert response.status_code == 200
    assert response.json()["result"] == "1.00000001"


def test_square_root_result_can_be_used_in_next_operation(client):
    square_root_response = client.post("/sqrt", json={"value": "25"})
    result = square_root_response.json()["result"]

    response = client.post(
        "/calculate",
        json={
            "first_number": result,
            "second_number": "2",
            "operation": "addition",
        },
    )

    assert response.status_code == 200
    assert response.json()["result"] == "7"


def test_calculator_page_and_assets_are_served(client):
    page = client.get("/")

    assert page.status_code == 200
    assert "Quick Arithmetic" in page.text
    assert 'aria-label="Square root"' in page.text
    assert '>√</button>' in page.text
    assert client.get("/static/style.css").status_code == 200
    assert client.get("/static/app.js").status_code == 200