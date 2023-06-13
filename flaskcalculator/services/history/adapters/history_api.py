from flaskcalculator.services.history.history_calculation import HistoryCalculation
from typing import List


def adapt(calculation_list: List[HistoryCalculation]) -> List[dict]:
    return [
        {
            "created": calculation.created.isoformat(),
            "operation": calculation.operation,
            "left_operand": calculation.left_operand,
            "right_operand": calculation.right_operand,
            "result": calculation.result,
        }
        for calculation in calculation_list
    ]
