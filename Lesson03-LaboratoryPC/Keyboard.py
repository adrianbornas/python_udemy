from InputDevice import InputDevice


class Keyboard(InputDevice):
    """
    Class to create keyboard objects
    """
    keyboard_count: int = 0

    @staticmethod
    def increase_keyboard_count():
        Keyboard.keyboard_count += 1

    def __init__(self, input_type: str, brand: str):
        InputDevice.__init__(self, input_type, brand)
        Keyboard.increase_keyboard_count()
        self._id_keyboard = Keyboard.keyboard_count

    @property
    def id_keyboard(self) -> int:
        return self._id_keyboard

    def __str__(self) -> str:
        return f'INPUT_DEVICE {self._id_keyboard} [ TYPE( {self._input_type} ) - BRAND( {self._brand} ) ]'
