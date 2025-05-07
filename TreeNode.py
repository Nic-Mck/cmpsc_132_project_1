# This is a class for Binary Tree
# Has 2 pointers(links):
#   the left pointing to the left child node
#   the right pointing to the right child node

class TreeNode:
    # Constructor
    def __init__(self, data):
        self.__data = data
        self.left = None
        self.right = None

    # Setters/Getters
    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    # Display/Printing
    def __str__(self):
        return f'{self.__data}'

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        if self.__data == other.get_data():
            return True
        else:
            return False