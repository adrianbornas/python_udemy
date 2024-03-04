from typing import TextIO


class FileHandler:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = None

    def __enter__(self) -> TextIO:
        print(f'Opening file {self.file_name}'.center(30, '-'))
        self.file = open(self.file_name, 'r', encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Closing file {self.file_name}'.center(30, '-'))
        if self.file:
            self.file.close()
