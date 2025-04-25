import typing

class Node :
    def __init__(self, data:typing.Any) -> None :
        self.__data = data
        self.__next = None

    def get_data(self) :
        return self.__data 
    
    def set_data(self, new_data) : 
        self.__data = new_data
    
    def get_next(self) : 
        return self.__next
    
    def set_next(self, new_next) : 
        self.__next = new_next