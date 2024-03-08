class CustomUser:
    def __init__(self, id_user: int = None, username: str = None, password: str = None):
        self._id_user = id_user
        self._username = username
        self._password = password

    @property
    def id_user(self) -> int:
        return self._id_user

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    def __str__(self):
        return f'USER ID {self._id_user} - {self._username} - {self._password}'
