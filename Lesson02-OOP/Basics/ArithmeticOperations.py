from typing import List


class ArithmeticOperations:
    """
    ArithmeticOperations class for do arithmetic operations
    """
    numbers: List[int | float]

    def sum(self) -> int | float:
        if len(self.numbers) == 1:
            return self.numbers.pop()
        else:
            return self.numbers.pop() + self.sum()

    def subtraction(self) -> int | float:
        if len(self.numbers) == 1:
            return self.numbers.pop()
        else:
            return self.numbers.pop() - self.subtraction()

    def multiplication(self) -> int | float:
        if len(self.numbers) == 1:
            return self.numbers.pop()
        else:
            return self.numbers.pop() * self.multiplication()

    def division(self) -> int | float:
        if len(self.numbers) == 1:
            return self.numbers.pop()
        else:
            return self.numbers.pop() / self.division()
