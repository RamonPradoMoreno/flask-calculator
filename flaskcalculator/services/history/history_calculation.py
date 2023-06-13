from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime


@dataclass
class HistoryCalculation:
    operation: str
    left_operand: Decimal
    right_operand: Decimal
    result: Decimal
    created: datetime = None

    @classmethod
    def from_dict(self, hist_dict):
        return HistoryCalculation(
            created=hist_dict.get("created"),
            operation=hist_dict.get("operation"),
            left_operand=hist_dict.get("left_operand"),
            right_operand=hist_dict.get("right_operand"),
            result=hist_dict.get("result"),
        )
