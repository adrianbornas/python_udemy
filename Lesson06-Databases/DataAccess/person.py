from logger_base import log


class Person:
    """
    Manage person objects
    """

    def __init__(self, person_id: int = None, name: str = None, surname: str = None, email: str = None):
        self._person_id = person_id
        self._name = name
        self._surname = surname
        self._email = email

    @property
    def person_id(self) -> int:
        return self._person_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        self._surname = surname

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    def __str__(self):
        return f'PERSON {self._person_id} - {self._name} {self._surname} - {self._email}'


if __name__ == '__main__':
    person1 = Person(1, 'Name', 'Surname', 'email@email.com')
    log.debug(person1)

    # Simulate insert
    person1 = Person(name='Name', surname='Surname', email='email@email.com')
    log.debug(person1)

    # Simulate delete
    person1 = Person(1)
    log.debug(person1)
