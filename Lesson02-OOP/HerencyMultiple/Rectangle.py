from HerencyMultiple.Color import Color
from HerencyMultiple.GeometricShape import GeometricShape


class Rectangle(GeometricShape, Color):
    def __init__(self, height: int, width: int, color: str):
        GeometricShape.__init__(self, height, width)
        Color.__init__(self, color)

    def calculate_area(self) -> int:
        return self.height * self.width

    def __str__(self) -> str:
        return f'RECTANGLE: {GeometricShape.__str__(self)} - {Color.__str__(self)}'
