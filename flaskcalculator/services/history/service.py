from flaskcalculator.services.history.ports.history import History
from flaskcalculator.services.calculator.calculation import Calculation
from typing import List
from flaskcalculator.db import get_db
from flaskcalculator.services.history.history_calculation import HistoryCalculation
from flaskcalculator.services.history.adapters import history_api
from flaskcalculator.services.history.history_calculation import HistoryCalculation

MAXIMUM_HISTORY_SIZE = 3


class HistoryService(History):
    def get_last_calculations(self) -> List[HistoryCalculation]:
        db = get_db()
        history = db.execute(
            "SELECT created, operation, left_operand, right_operand, result " " FROM history" " ORDER BY created DESC"
        ).fetchmany(MAXIMUM_HISTORY_SIZE)
        return [HistoryCalculation.from_dict(dict(row)) for row in history]

    def save_new_calculation(self, calculation: HistoryCalculation) -> None:
        db = get_db()
        db.execute(
            "INSERT INTO history (operation, left_operand, right_operand, result)" " VALUES (?, ?, ?, ?)",
            (
                calculation.operation,
                str(calculation.left_operand),
                str(calculation.right_operand),
                str(calculation.result),
            ),
        )
        db.commit()
