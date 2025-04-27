# Names: Nick McKenna, Edward Hu
# Class: CMPSC132
# Date of Final Revision: 4-27-2025

# This module represents a node with wrapped data in our LinkedList ADT
# As specified, encapsulated data is wrapped into a node

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