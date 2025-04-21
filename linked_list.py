import typing
import node

class LinkedList :
    def __init__(self) -> None :
        self.head = None
        self.tail = None

    def insert_node_after(self, after_data:typing.Any, data:typing.Any) -> None :
        new_node = node.Node(data)

        if after_data == "Null" :
            new_node.next = self.head
            self.head = new_node
            return
        if self.head.data == after_data :
            temp = self.head.next
            new_node.next = temp
            self.head.next = new_node
        else :
            curr_node = self.head
            while curr_node.data != after_data and curr_node.next is not None :
                curr_node = curr_node.next

            # Once element to insert after is found, or we reach the end of the list, insert new node
            new_node.next = curr_node.next
            curr_node.next = new_node

    def insert_node_sorted(self, data:typing.Any) -> None :
        new_node = node.Node(data)
        curr_node = self.head
        if curr_node is None or curr_node.data > new_node.data :
            new_node.next = self.head
            self.head = new_node
        else :
            while curr_node.next is not None :
                if curr_node.next.data > new_node.data :
                    new_node.next = curr_node.next
                    curr_node.next = new_node

                    if new_node.next is None :
                        self.tail = new_node

                    return
                curr_node = curr_node.next

            self.append_node(data)

    def append_node(self, data:typing.Any) -> None :
        new_node = node.Node(data)

        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node


    def prepend_node(self, data:typing.Any) -> None :
        new_node = node.Node(data)

        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node


    def display(self) -> None :
        print("AH")
        if not self.head : return None
        
        node = self.head
        while True :
            print(node.data, end="")
            node = node.next

            if node is not None :
                print(" -> ", end="")
            else :
                print()
                break

    def __str__(self) -> str : 
        if not self.head : return ""

        ret_str:str = ''

        node = self.head 
        while node : 
            ret_str += str(node.data)
            node = node.next 
            ret_str += "\n"

        return ret_str

    def search(self, key:typing.Any) -> node.Node | None :
        current_node = self.head
        while current_node is not None :
            if current_node.data == key :
                print(f'Key: {key} found.')
                return current_node

            current_node = current_node.next

        return None

    def remove_data(self, key=typing.Any) -> int :
        # If first element is the one to be deleted
        if self.head.data == key :
            self.head = self.head.next
            return 1

        # Find and skip requested element
        current_node = self.head
        while current_node is not None :

            if current_node.next.data == key :
                current_node.next = current_node.next.next

                if current_node.next is None :
                    self.tail = current_node
                return 1

            current_node = current_node.next

        return -1