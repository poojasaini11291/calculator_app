from fastapi import APIRouter, HTTPException

from src.calculator import (
    calculate,
    calculate_square_root,
    format_square_root_result,
)
from src.schemas import (
    CalculationRequest,
    CalculationResponse,
    SquareRootRequest,
    SquareRootResponse,
)

router = APIRouter()


@router.post("/calculate", response_model=CalculationResponse)
def calculate_numbers(request: CalculationRequest) -> CalculationResponse:
    try:
        result = calculate(
            request.first_number,
            request.second_number,
            request.operation,
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error

    return CalculationResponse(result=format(result.normalize(), "f"))


@router.post("/sqrt", response_model=SquareRootResponse)
def calculate_square_root_value(
    request: SquareRootRequest,
) -> SquareRootResponse:
    try:
        result = calculate_square_root(request.value)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error

    return SquareRootResponse(result=format_square_root_result(result))