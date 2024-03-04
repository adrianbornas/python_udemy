class Cube:
    def __init__(self, width: int | float, depth: int | float, height: int | float):
        self._width = width
        self._depth = depth
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, depth):
        self._depth = depth

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def calculate_volume(self) -> int | float:
        return self._width * self._depth * self._height

    def __del__(self):
        print('Cube deleted'.center(30, '-'))
        print(f'''DATA:
    With: {self._width}
    Depth: {self._depth}
    Height: {self._height}
''')


if __name__ == '__main__':
    print('This message only appears when the file Cube.py is executed directly, not from import')
