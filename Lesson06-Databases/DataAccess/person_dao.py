from typing import List

from DataAccess.constants import SELECT_PERSON, INSERT_PERSON, UPDATE_PERSON, DELETE_PERSON
from DataAccess.cursor_db import CursorDB
from DataAccess.person import Person
from logger_base import log


class PersonDAO:
    """
    Data Access Object for person entity
    """

    @classmethod
    def select(cls) -> List[Person]:
        with CursorDB() as cursor:
            cursor.execute(SELECT_PERSON)
            results = cursor.fetchall()
            person_list = []
            for row in results:
                person_list.append(Person(row[0], row[1], row[2], row[3]))
            return person_list

    @classmethod
    def insert(cls, person_data: Person):
        with CursorDB() as cursor:
            values = (person_data.name, person_data.surname, person_data.email)
            log.debug(f'INSERT: {person_data} ')
            cursor.execute(INSERT_PERSON, values)
            log.debug(f'Inserted {cursor.rowcount} rows')

    @classmethod
    def update(cls, person_data: Person, person_id: int):
        with CursorDB() as cursor:
            values = (person_data.name, person_data.surname, person_data.email, person_id)
            log.debug(f'UPDATE: {person_data} ')
            cursor.execute(UPDATE_PERSON, values)
            log.debug(f'Updated {cursor.rowcount} rows')

    @classmethod
    def delete(cls, person_data: Person):
        with CursorDB() as cursor:
            log.debug(f'DELETE ID: {person_data.person_id} ')
            cursor.execute(DELETE_PERSON, (person_data.person_id,))
            log.debug(f'Deleted {cursor.rowcount} rows')


if __name__ == '__main__':
    # SELECT
    list_person = PersonDAO.select()
    for person in list_person:
        log.debug(person)

    # INSERT
    data = Person(name='Name', surname='Surname', email='email@test.com')
    PersonDAO.insert(data)

    list_person = PersonDAO.select()
    last_person = None
    for person in list_person:
        last_person = person
        log.debug(person)

    # UPDATE
    data = Person(name='NameUpd', surname='SurnameUpd', email='emailUpd@test.com')
    PersonDAO.update(data, last_person.person_id)

    list_person = PersonDAO.select()
    for person in list_person:
        log.debug(person)

    # DELETE
    data = Person(person_id=last_person.person_id)
    PersonDAO.delete(data)

    list_person = PersonDAO.select()
    for person in list_person:
        log.debug(person)
