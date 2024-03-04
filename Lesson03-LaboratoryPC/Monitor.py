class Monitor:
    """
    Class to create monitor objects
    """
    monitor_count: int = 0

    @staticmethod
    def increase_monitor_count():
        Monitor.monitor_count += 1

    def __init__(self, brand: str, size: int):
        Monitor.increase_monitor_count()
        self._id_monitor = Monitor.monitor_count
        self._brand = brand
        self._size = size

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        self._brand = brand

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int):
        self._size = size

    def __str__(self) -> str:
        return f'MONITOR {self._id_monitor} [ BRAND( {self._brand} ) - SIZE( {self._size} ) ]'
