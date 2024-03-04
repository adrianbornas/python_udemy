from HerencyMultiple.Color import Color
from HerencyMultiple.GeometricShape import GeometricShape


class Square(GeometricShape, Color):
    def __init__(self, side: int, color: str):
        GeometricShape.__init__(self, side, side)
        Color.__init__(self, color)

    def calculate_area(self) -> int:
        return self.height * self.width

    def __str__(self) -> str:
        return f'SQUARE: {GeometricShape.__str__(self)} - {Color.__str__(self)}'
