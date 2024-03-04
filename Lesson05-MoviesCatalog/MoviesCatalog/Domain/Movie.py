class Movie:
    """
    Representation of movie object
    """
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return f'{self._name}'