import typing

class Node :
    def __init__(self, data:typing.Any) -> None :
        self.data = data
        self.next = None