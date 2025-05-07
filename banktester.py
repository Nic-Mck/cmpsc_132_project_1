from BankAccount import *
from linked_list import LinkedList
from node import Node
from MyBST import MyBST
from MyQueue import MyQueue
from TreeNode import TreeNode

"""Note: Except for sorting the BST all are implemented. the Tester for BST search is not sorting properly as 
the get_total_balance() method in Customer Class in BankAccount.py has a logic error"""

def main():
    # Create Customer Queue
    customer_queue = MyQueue()

    # Create 5 Customers & Add their accounts using Linked List as specified
    c1 = Customer("Joe")
    a1 = Account(0, 'test', 500)
    a2 = Account(1, 'test', 1000, "savings")
    a3 = Account(2, 'test',10000, 'retirement')
    c1.add_account(a1)
    c1.add_account(a2)
    c1.add_account(a3)

    c2 = Customer("Ivy")
    a4 = Account(3, 'test', 5000)
    #a5 = Account(4, 'test', 0, "savings")
    a6 = Account(5, 'test', 8000, 'retirement')
    c2.add_account(a4)
    #c2.add_account(a5)
    c2.add_account(a6)

    c3 = Customer("Sam")
    #a7 = Account(6, 'test', 0)
    a8 = Account(7, 'test', 2000, "savings")
    a9 = Account(8, 'test', 12000, 'retirement')
    #c3.add_account(a7)
    c3.add_account(a8)
    c3.add_account(a9)

    c4 = Customer("Jun")
    a10 = Account(9, 'test', 4500)
    a11 = Account(10, 'test', 1500, "savings")
    a12 = Account(11, 'test', 6500, 'retirement')
    c4.add_account(a10)
    c4.add_account(a11)
    c4.add_account(a12)

    c5 = Customer("Kate")
    a13 = Account(12, 'test', 3000)
    a14 = Account(13, 'test', 8000, "savings")
    #a15 = Account(14, 'test', 0, 'retirement')
    c5.add_account(a13)
    c5.add_account(a14)
    #c5.add_account(a15)

    customer_queue.enQueue(c1)
    customer_queue.enQueue(c2)
    customer_queue.enQueue(c3)
    customer_queue.enQueue(c4)
    customer_queue.enQueue(c5)

    # Retrieve all total balances in Customer Queue & calc interest rate to add bonus
    #FIXME - not displaying by order of total balance & calculating interest not finished
    customer_queue.display()

    # Create BST & Add Customers
    customer_bst = MyBST()

    customer_bst.add_data(c1)
    customer_bst.add_data(c2)
    customer_bst.add_data(c3)
    customer_bst.add_data(c4)
    customer_bst.add_data(c5)

    customer_bst.display()

    # FIXME - did not finish due to > error
    #customer_bst.search("Sam")


if __name__ == "__main__":
    main()