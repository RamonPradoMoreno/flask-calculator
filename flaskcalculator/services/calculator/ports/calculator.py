import abc
from flaskcalculator.services.calculator.calculation import Calculation


class Calculator(abc.ABC):
    @abc.abstractmethod
    def calculate(self, calculation: Calculation) -> float:
        pass
