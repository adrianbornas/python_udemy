from typing import List
from Computer import Computer


class Order:
    """
    Class to create order objects and store computer objects
    """
    order_count: int = 0

    @staticmethod
    def increase_order_count():
        Order.order_count += 1

    def __init__(self, computers: List[Computer]):
        Order.increase_order_count()
        self._id_order = Order.order_count
        self._computers = list(computers)

    @property
    def id_order(self) -> int:
        return self._id_order

    @property
    def computers(self) -> list[Computer]:
        return self._computers

    @computers.setter
    def computers(self, computers: List[Computer]):
        self._computers = list(computers)

    def add_computer(self, computer: Computer):
        self._computers.append(computer)

    def __str__(self) -> str:
        computers_str = ''
        for computer in self._computers:
            computers_str += computer.__str__() + '\n'

        return f'ORDER {self._id_order} \n {computers_str}'
