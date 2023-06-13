from flaskcalculator.services.calculator.calculation import Calculation
from flaskcalculator.services.calculator.ports.calculator import Calculator
from decimal import Decimal, getcontext, InvalidOperation
from flaskcalculator.services.calculator.calculation import SupportedCalculation
from flaskcalculator.services.calculator.adapters import calculator_history as calculator_history_adapter

# Set the maximum precision to x digits
# This is important due to how floating point works in Python
# Try doing 1.1 + 2.1 in the console
getcontext().prec = 12


class AdditionService(Calculator):
    def calculate(self, calculation: Calculation) -> float:
        result = float(calculation.left_operand + calculation.right_operand)
        calculator_history_adapter.adapt(
            left_operand=calculation.left_operand,
            right_operand=calculation.right_operand,
            result=result,
            operation=calculation.type,
        )
        return result


calculator_service_factory = {SupportedCalculation.ADDITION.value: AdditionService}
