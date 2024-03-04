from abc import ABC, abstractmethod

from HerencyMultiple.constants import MAX_SIDE_VALUE


class GeometricShape(ABC):
    def __init__(self, height: int, width: int):
        self._height = self._validate_side_value(height)
        self._width = self._validate_side_value(width)

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = self._validate_side_value(height)

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width):
        self._width = self._validate_side_value(width)

    @abstractmethod
    def calculate_area(self) -> int:
        pass

    @staticmethod
    def _validate_side_value(value: int) -> int:
        return value if 0 <= value <= MAX_SIDE_VALUE else 0

    def __str__(self) -> str:
        return f'HEIGHT {self._height} - WIDTH {self._width}'
