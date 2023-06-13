# define Python user-defined exceptions
class CalculatorError(Exception):
    "Raised when there is an error in Calculator Service"

    def __init__(self, message="Unknown error in Calculator Service"):
        self.message = message
        super().__init__(self.message)


class OperandError(CalculatorError):
    "Raised when an operand cannot be converted to Decimal"

    def __init__(self, message="At least one operand is not a number"):
        self.message = message
        super().__init__(self.message)


class MissingOperandError(CalculatorError):
    "Raised when an operand cannot be converted to Decimal because it's None"

    def __init__(self, message="At least one operand is missing"):
        self.message = message
        super().__init__(self.message)
