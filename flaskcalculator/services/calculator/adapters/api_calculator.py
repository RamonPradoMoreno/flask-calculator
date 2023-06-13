from flaskcalculator.services.calculator.calculation import SupportedCalculation
from flaskcalculator.services.calculator.ports.calculator import Calculator
from flaskcalculator.services.calculator.calculation import calculation_factory
from decimal import Decimal, InvalidOperation
from flaskcalculator.services.calculator.service import calculator_service_factory
from flaskcalculator.services.calculator.errors import MissingOperandError, OperandError


def adapt(left_operand: str, right_operand: str, operation: str) -> float:
    try:
        # Decimal has been used to avoid float rounding problems
        left_operand = Decimal(left_operand)
        right_operand = Decimal(right_operand)
    except TypeError:
        raise MissingOperandError()
    except InvalidOperation:
        raise OperandError()

    try:
        calculation = calculation_factory.get(operation)(left_operand=left_operand, right_operand=right_operand)
        calculator_service = calculator_service_factory.get(operation)()
        return calculator_service.calculate(calculation=calculation)
    except Exception:
        raise NotImplementedError("Only Addition has been implemented")
