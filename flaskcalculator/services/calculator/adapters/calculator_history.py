from decimal import Decimal
from flaskcalculator.services.history.history_calculation import HistoryCalculation
from flaskcalculator.services.history.service import HistoryService


def adapt(operation: str, left_operand: Decimal, right_operand: Decimal, result: float):
    calculation = HistoryCalculation(
        left_operand=left_operand, right_operand=right_operand, result=result, operation=operation
    )
    HistoryService().save_new_calculation(calculation=calculation)
