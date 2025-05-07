# Names: Nick McKenna, Edward Hu
# Class: CMPSC132
# Date of Final Revision: 4-27-2025

# This module represents our custom LinkedList ADT
# Used in the Student() class for their course list attribute in Student.py
# Used in the Advisor() class for their Student() list (advisee list) attribute in Advisor.py

import typing
import node

# Linked List ADT (singly linked)
class LinkedList :
    def __init__(self) -> None :
        self.head = None
        self.tail = None

    def insert_node_after(self, after_data:typing.Any, data:typing.Any) -> None :
        new_node = node.Node(data)

        if after_data == "Null" :
            new_node.set_next(self.head)
            self.head = new_node
            return
        if self.head.get_data() == after_data :
            temp = self.head.get_next()
            new_node.set_next(temp)
            self.head.set_next(new_node)
        else :
            curr_node = self.head
            while curr_node.get_data() != after_data and curr_node.get_next() is not None :
                curr_node = curr_node.get_next()

            # Once element to insert after is found, or we reach the end of the list, insert new node
            new_node.set_next(curr_node.get_next())
            curr_node.set_next(new_node)

    def insert_node_sorted(self, data:typing.Any) -> None :
        new_node = node.Node(data)
        curr_node = self.head
        if curr_node is None or curr_node.get_data() > new_node.get_data() :
            new_node.set_next(self.head)
            self.head = new_node
        else :
            while curr_node.get_next() is not None :
                if curr_node.get_next().get_data() > new_node.get_data() :
                    new_node.set_next(curr_node.get_next())
                    curr_node.set_next(new_node)

                    if new_node.get_next() is None :
                        self.tail = new_node

                    return
                curr_node = curr_node.get_next()

            self.append_node(data)

    def append_node(self, data:typing.Any) -> None :
        new_node = node.Node(data)

        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.set_next(new_node)
            self.tail = new_node


    def prepend_node(self, data:typing.Any) -> None :
        new_node = node.Node(data)

        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            new_node.set_next(self.head)
            self.head = new_node


    def display(self) -> None :
        if not self.head : 
            #print("No Nodes")
            #print("\nNotice: No Advisees in your Student List currently")
            print(f"\nNotice: No Accounts in your profile")
            return 
        
        node = self.head
        while True :
            print(node.get_data(), end="")
            node = node.get_next()

            if node is not None :
                print()
                #print(" -> ", end="")
            else :
                print()
                break

    def __str__(self) -> str : 
        if not self.head : return ""

        ret_str:str = ''

        node = self.head 
        while node : 
            ret_str += str(node.get_data())
            node = node.get_next()
            ret_str += "\n"

        return ret_str

    def search(self, key:typing.Any) -> node.Node | None :
        current_node = self.head
        while current_node is not None :
            if current_node.get_data().get_id_num() == key :
                #print(f'Key: {key} found.')
                return current_node.get_data()

            current_node = current_node.get_next()

        return None

    def remove_data(self, key=typing.Any) -> int :
        # If first element is the one to be deleted
        if self.head.get_data() == key :
            self.head = self.head.get_next()
            return 1

        # Find and skip requested element
        current_node = self.head
        while current_node.get_next() is not None :

            if current_node.get_next().get_data() == key :
                current_node.set_next(current_node.get_next().get_next())

                if current_node.get_next() is None :
                    self.tail = current_node
                return 1

            current_node = current_node.get_next()

        return -1