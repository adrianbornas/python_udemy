from typing import List

from constants import SELECT_USER, INSERT_USER, UPDATE_USER, DELETE_USER
from cursor_db import CursorDB
from custom_user import CustomUser
from logger_base import log


class CustomUserDao:
    """
    CRUD operations over CustomUser entity
    """
    @classmethod
    def select(cls) -> List[CustomUser]:
        user_list = []
        with CursorDB() as cursor:
            log.debug(f'Select users')
            cursor.execute(SELECT_USER)
            result = cursor.fetchall()
            for row in result:
                user = CustomUser(row[0], row[1], row[2])
                user_list.append(user)
        return user_list

    @classmethod
    def insert(cls, user: CustomUser) -> int:
        with CursorDB() as cursor:
            log.debug(f'User to insert {user}')
            values = (user.username, user.password)
            cursor.execute(INSERT_USER, values)
            return cursor.rowcount

    @classmethod
    def update(cls, user: CustomUser) -> int:
        with CursorDB() as cursor:
            log.debug(f'User to update {user}')
            values = (user.username, user.password, user.id_user)
            cursor.execute(UPDATE_USER, values)
            return cursor.rowcount

    @classmethod
    def delete(cls, user: CustomUser) -> int:
        with CursorDB() as cursor:
            log.debug(f'User to delete {user}')
            cursor.execute(DELETE_USER, (user.id_user,))
            return cursor.rowcount
