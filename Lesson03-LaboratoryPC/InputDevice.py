from abc import ABC, abstractmethod


class InputDevice(ABC):
    """
    Class to create input device objects
    """
    def __init__(self, input_type: str, brand: str):
        self._input_type = input_type
        self._brand = brand

    @property
    def input_type(self) -> str:
        return self._input_type

    @input_type.setter
    def input_type(self, input_type: str):
        self._input_type = input_type

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        self._brand = brand

    @abstractmethod
    def __str__(self) -> str:
        pass
