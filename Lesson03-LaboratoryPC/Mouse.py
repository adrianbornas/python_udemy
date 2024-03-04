from InputDevice import InputDevice


class Mouse(InputDevice):
    """
    Class to create mouse objects
    """
    mouse_count: int = 0

    @staticmethod
    def increase_mouse_count():
        Mouse.mouse_count += 1

    def __init__(self, input_type: str, brand: str):
        InputDevice.__init__(self, input_type, brand)
        Mouse.increase_mouse_count()
        self._id_mouse = Mouse.mouse_count

    @property
    def id_keyboard(self) -> int:
        return self._id_mouse

    def __str__(self) -> str:
        return f'MOUSE {self._id_mouse} [ TYPE( {self._input_type} ) - BRAND( {self._brand} ) ]'
