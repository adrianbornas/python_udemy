class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, base: int | float, height: int | float):
        self.base = base
        self.height = height

    def calculate_area(self) -> int | float:
        return self.base * self.height
