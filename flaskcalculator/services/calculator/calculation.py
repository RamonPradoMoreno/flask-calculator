from abc import abstractmethod, ABC
from enum import Enum
from dataclasses import dataclass
from decimal import Decimal


class SupportedCalculation(Enum):
    ADDITION = "addition"


@dataclass
class Calculation(ABC):
    @property
    @abstractmethod
    def type(self):
        pass


@dataclass
class Addition(Calculation):
    left_operand: Decimal
    right_operand: Decimal

    @property
    def type(self):
        return SupportedCalculation.ADDITION.value


calculation_factory = {SupportedCalculation.ADDITION.value: Addition}
