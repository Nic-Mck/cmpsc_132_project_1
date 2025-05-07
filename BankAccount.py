from linked_list import LinkedList
from node import Node
from MyBST import MyBST
from TreeNode import TreeNode
from MyQueue import MyQueue

class Account:

    valid_account_types = ["checking", "savings", "retirement"]

    def __init__(self, account_num = 0, password = "", balance = 0.0, account_type = "Checking"):
        self.__account_num = account_num
        self.__password = password
        self.__balance = balance
        self.__account_type = account_type

    def _authenticate(self, a_password):
        if self.__password == a_password:
            print(f"Authenticated")
            return True
        else:
            print(f"Authentication not passed")
            return False

    def change_password(self, o_password, n_password):
        if self.__password == o_password:
            self.__password = n_password
        else:
            print(f"Error: Please enter correct current password to change to new password")
            self.__password = o_password

    def deposit(self, amount, a_password):
        if self.__password == a_password:
            self.__balance += amount
            print(f"Amount: ${amount} successfully deposited to account")
        else:
            print(f'Error: Password incorrect')

    def withdraw(self, amount, a_password):
        if self.__password == a_password:
            if self.__balance < amount:
                print(f"Error: Cannot withdraw, insufficient funds in your account")
            else:
                self.__balance -= amount
                print(f"Amount: ${amount} successfully withdrawn from account")
        else:
            print(f"Error: Password incorrect")

    def get_balance(self):
        return round(self.__balance, 2)

    def set_account_type(self, account_type):
        if account_type.strip().lower() in self.valid_account_types:
            self.__account_type = account_type
        else:
            print(f"Error: Please enter a valid account type [checking/savings/retirement]")

    def get_account_type(self):
        return self.__account_type

    def __str__(self):
        return f'Account Type: {self.__account_type}, Balance: {self.__balance}'


class Customer:
    def __init__(self, name=""):
        self.__name = name
        self.__accounts = LinkedList()

    def get_name(self):
        return self.__name

    def add_account(self, account):
        self.__accounts.append_node(account)

    #FIXME - logic error, affects output in tester module so was unable to sort by total balance as specified
    """Other than this, the tester module with ADT verification works"""
    def get_total_balance(self):
        total_bal = 0
        while self.__accounts.head is not None:
            single_bal = self.__accounts.head.get_data().get_balance()
            self.__accounts.head = self.__accounts.head.next
            #return self.__accounts.head.get_data().get_balance()
            while not self.__accounts.tail.next:
                total_bal += single_bal
                return total_bal


    def remove_account(self, account_num):
        if account_num in self.__accounts:
            self.__accounts.remove_data(account_num)
        else:
            print(f"Error: {account_num} not found in the list")

    def search_account(self, account_num):
        self.__accounts.search(account_num)

    def __str__(self):
        return f"Customer Name: {self.__name}, Total Balance: ${self.get_total_balance()}"

    # FIXME - Has logic error
    def __gt__(self, other):
        if self.__name > other.get_name():
            return True
        else:
            return False


if __name__ == "__main__":
    a1 = Account(0, "test", 499.94)
    a2 = Account(1, 'test', 1000)
    #print(a1)

    c1 = Customer("Joe Tester")
    c1.add_account(a1)
    c1.add_account(a2)
    print(c1)