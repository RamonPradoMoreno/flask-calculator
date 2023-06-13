import abc
from flaskcalculator.services.history.history_calculation import HistoryCalculation
from typing import List


class History(abc.ABC):
    @abc.abstractmethod
    def get_last_calculations(self) -> List[HistoryCalculation]:
        pass

    @abc.abstractmethod
    def save_new_calculation(self, calculation: HistoryCalculation) -> None:
        pass
