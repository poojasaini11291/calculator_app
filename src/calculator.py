from decimal import Decimal, ROUND_HALF_UP, localcontext

from src.schemas import Operation

SQUARE_ROOT_PRECISION = 8
SQUARE_ROOT_ERROR = "Invalid input. Square root of a negative number is not supported."


def calculate(
    first_number: Decimal,
    second_number: Decimal,
    operation: Operation,
) -> Decimal:
    if operation == "addition":
        return first_number + second_number
    if operation == "subtraction":
        return first_number - second_number
    if operation == "multiplication":
        return first_number * second_number
    if operation == "division":
        if second_number == 0:
            raise ValueError("The second number must not be zero for division.")
        return first_number / second_number
    raise ValueError("Unsupported operation.")


def calculate_square_root(value: Decimal) -> Decimal:
    if value < 0:
        raise ValueError(SQUARE_ROOT_ERROR)
    if value == 0:
        return Decimal(0)

    integer_digits = max(1, value.adjusted() // 2 + 1)
    with localcontext() as context:
        context.prec = max(context.prec, integer_digits + 10)
        result = value.sqrt().quantize(
            Decimal(1).scaleb(-SQUARE_ROOT_PRECISION),
            rounding=ROUND_HALF_UP,
        )
    return result


def format_square_root_result(value: Decimal) -> str:
    result = format(value, "f")
    if "." in result:
        result = result.rstrip("0").rstrip(".")
    return result