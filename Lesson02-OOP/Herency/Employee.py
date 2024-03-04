from Herency.Person import Person


class Employee(Person):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self._salary = salary

    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, salary: int):
        self._salary = salary

    def __str__(self) -> str:
        return f'{super().__str__()} and gains {self._salary}'
