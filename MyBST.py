# This is a Binary Search Tree
# Each TreeNode has a maximum of 2 children
# Sorted by Key: the left child < node <= right node

from TreeNode import TreeNode
#from Circle import Circle

class MyBST:
    # Constructor
    def __init__(self):
        self.root = None    # Creates an empty Binary Search Tree

    # Add a TreeNode
    def add_data(self, data):
        n_node = TreeNode(data)     # Wrap data into a TreeNode
        if not self.root: # If BST is empty
            self.root = n_node
        else:   # Non-empty BST; find the proper position for the new node
            t_pointer = self.root   # Traversal pointer to find proper position
            # Traversal loop
            while t_pointer:
                # Goes to left side of BST if new data < root till leaf reached
                if t_pointer.get_data() > data: # Assume primitive data (for now)

                    if t_pointer.left:  # If left pointer not empty, keep traversing down left side of BST
                        t_pointer = t_pointer.left
                    else: # Position is found
                        t_pointer.left = n_node
                        break
                # Else goes to right side of BST if new data > root until leaf reached
                else:
                    if t_pointer.right: # If right pointer not empty, keep traversing down right side of BST
                        t_pointer = t_pointer.right
                    else:
                        t_pointer.right = n_node
                        break

        print(f'Customer info ({data}) has been added!')

    def test_remove_data(self, key):
        # If Tree Empty
        if not self.root:
            print(f"Notice: Empty Tree")
            return None
        # Traversal
        parent = None
        current = self.root

        while current:
            # If Node Found
            if current.get_data() == key:
                # Removing Leaf Node (root & non-root)
                if not current.left and not current.right:

                    if not parent:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                # Remove root if only left child exists
                elif not current.right:
                    if not parent:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                # Remove root if only right child exists
                elif not current.left:
                    if not parent:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                # Remove if both children exist (middle node removal)
                else:
                    successor = current.right
                    successor_parent = current
                    while successor.left:
                        successor_parent = successor
                        successor = successor.left
                    # Replace current with successor data
                    current.set_data(successor.get_data())
                    # Delete successor node
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right

                #print(f"Node removed from BST successfully!")
                return True
            # Traverse left or right for node to remove
            elif current.get_data() < key:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        #print(f"Error: Node not found in BST, cannot remove")
        return False

    # Search
    def search(self, key):
        current = self.root
        while current:
            if key == current.get_data():
                # Case when key is found in BST
                print(f"{key} has been found in BST!")
                return current
            elif key < current.get_data():
                # Searches the left subtree
                current = current.left
            else:
                # Searches the right subtree
                current = current.right

        # Case When Node not found in search
        print(f"{key} not found in the BST")
        return None

    # Edit

    # Display/Printing
    """#NOTE: Recursive Algorithm is recommended to display BST"""

    def display(self):
        self._display(self.root)

    def _display(self, node):
        if not node:
            #print(f'Notice: Empty')
            return None
        else:
            if node.left:
                self._display(node.left)
            print(node, end='-->')

            if node.right:
                self._display(node.right)

if __name__ =='__main__':

    print("Adding Data Test")
    bst1 = MyBST()
    """c1 = Circle(15)
    c2 = Circle(10)
    c3 = Circle(2.5)
    c4 = Circle(20)
    c5 = Circle(12.5)

    bst1.add_data(c1)
    bst1.add_data(c2)
    bst1.add_data(c3)
    bst1.add_data(c4)
    bst1.add_data(c5)"""

    bst1.add_data(500)
    bst1.add_data(750)
    bst1.add_data(200)
    bst1.add_data(150)
    bst1.add_data(201)
    bst1.add_data(950)
    bst1.add_data(850)
    bst1.add_data(550)
    bst1.add_data(650)
    bst1.add_data(875)

    #bst1.display()

    #print()
    bst1.add_data(800)
    bst1.add_data(100)
    bst1.add_data(600)
    bst1.add_data(1)

    print()
    print("Updated Tree (Display Test):")
    bst1.display()
    print()

    print()
    print("Removing Root Test")
    bst1.test_remove_data(500)
    #print("Removing Root (500):")
    bst1.display()
    print()
    print()

    print()
    print("Removing Middle Node Test")
    bst1.test_remove_data(750)
    bst1.display()
    print()
    print()

    print()
    print("Removing Leaf Node Test")
    bst1.test_remove_data(1)
    bst1.display()
    print()

    print()
    print("Invalid Removal Test")
    bst1.test_remove_data(-22)
    print()

    print("BST Search Test (Found or Not Found)")
    bst1.search(0)
    bst1.search(100)
