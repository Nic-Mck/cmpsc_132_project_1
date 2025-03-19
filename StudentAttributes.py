# Names: Nick McKenna, Edward Hu
# Class: CMPSC132
# Date of Final Revision: 3-18-2025

# This module defines attribute ADTs for the Student class

class Address:

    def __init__(self, street_address='', city='', state='', zip_code='', address_type=''):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__address_type = address_type

    def set_street_address(self, street_address):
        if len(street_address) != 0:
            self.__street_address = street_address
        else:
            print(f'Error: Street Address Blank')

    def get_street_address(self):
        return self.__street_address

    def set_city(self, city):
        if len(city) != 0:
            self.__city = city
        else:
            print(f'Error: City Blank')

    def get_city(self):
        return self.__city

    def set_state(self, state):
        if len(state) != 0:
            self.__state = state
        else:
            print(f'Error: State Blank')

    def get_state(self):
        return self.__state

    def set_zip_code(self, zip_code):
        if len(zip_code) != 0:
            self.__zip_code = zip_code
        else:
            print(f'Error: Zip Code Blank')

    def get_zip_code(self):
        return self.__zip_code

    def set_address_type(self, address_type):
        if len(address_type) != 0:
            self.__address_type = address_type
        else:
            print(f'Error: Address Type Blank')

    def display(self):
        print(f'{self.__street_address}, {self.__city}, {self.__state} {self.__zip_code}')

    def __str__(self):
        return f'{self.__street_address}, {self.__city}, {self.__state} {self.__zip_code}'

class EmailAddress:

    def  __init__(self, address='', email_type=''):
        self.__address = address
        self.__email_type = email_type

    def set_address(self, address):
        if len(address) != 0:
            self.__address = address
        else:
            print(f'Error: Email Address Blank')

    def get_address(self):
        return self.__address

    def set_email_type(self, email_type):
        if len(email_type) != 0:
            self.__email_type = email_type
        else:
            print(f'Error: Email Type Blank')

    def get_email_type(self):
        return self.__email_type

    def display(self):
        print(f'    {self.__address}, ({self.__email_type})')

    def __str__(self):
        return f'    {self.__address}, ({self.__email_type})'

    def append(self, i):
        pass

class PhoneNumber:

    def __init__(self, phone_number='', phone_type=''):
        self.__phone_number = phone_number
        self.__phone_type = phone_type

    def set_phone_number(self, phone_number):
        if len(phone_number) != 0:
            self.__phone_number = phone_number
        else:
            print(f'Error: Phone Number Blank')

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_type(self, phone_type):
        if len(phone_type) != 0:
            self.__phone_type = phone_type
        else:
            print(f'Error: Phone Type Blank')

    def get_phone_type(self):
        return self.__phone_type

    def display(self):
        print(f'    {self.__phone_number}, ({self.__phone_type})')

    def __str__(self):
        return f'    {self.__phone_number}, ({self.__phone_type})'


if __name__ == '__main__':

    # Address ADT Test
    address1 = Address('5066 Portola Drive', 'Rockford Hills', 'CA', '97707',
                 'Residential')

    print(address1)

    # EmailAddress ADT Test
    email1 = EmailAddress('info@tunerdesign.org', 'Business')
    print(email1)

    # PhoneNumber ADT Test
    phone1 = PhoneNumber('610-303-3023', 'Cell')
    print(phone1)
