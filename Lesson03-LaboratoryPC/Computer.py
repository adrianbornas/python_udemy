from Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse


class Computer:
    """
    Class to create computer objects
    """
    computer_count: int = 0

    @staticmethod
    def increase_computer_count():
        Computer.computer_count += 1

    def __init__(self, name: str, monitor: Monitor, keyboard: Keyboard, mouse: Mouse):
        Computer.increase_computer_count()
        self._id_computer = Computer.computer_count
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    @property
    def id_computer(self) -> int:
        return self._id_computer

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def monitor(self) -> Monitor:
        return self._monitor

    @monitor.setter
    def monitor(self, monitor: Monitor):
        self._monitor = monitor

    @property
    def keyboard(self) -> Keyboard:
        return self._keyboard

    @keyboard.setter
    def keyboard(self, keyboard: Keyboard):
        self._keyboard = keyboard

    @property
    def mouse(self) -> Mouse:
        return self._mouse

    @mouse.setter
    def mouse(self, mouse: Mouse):
        self._mouse = mouse

    def __str__(self) -> str:
        return f'COMPUTER {self._id_computer} [ NAME( {self._name} )]\n\t {self.monitor}\n\t {self.keyboard}\n\t {self.mouse}'
