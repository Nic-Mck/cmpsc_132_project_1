# Names: Nick McKenna, Edward Hu
# Class: CMPSC132
# Date of Final Revision: 3-18-2025

# This module defines attribute ADTs for the Student class

class Name:

    def __init__(self, first='', middle='', last=''):
        self.__first = first
        self.__middle = middle
        self.__last = last

    def set_first(self, first):
        if len(first) != 0:
            self.__first = first
        else:
            print(f'Error: First Name Blank')

    def get_first(self):
        return self.__first

    def set_middle(self, middle):
        self.__middle = middle      

    def get_middle(self):
        return self.__middle
    
    def set_last(self, last):
        if len(last) != 0:
            self.__last = last
        else:
            print(f'Error: Last Name Blank')

    def get_last(self):
        return self.__last
    
    def display(self):
        if len(self.get_middle()) != 0: 
            print(f'{self.__first} {self.__middle} {self.__last}')
        else:
            print(f'{self.__first} {self.__last}')
    
    def __str__(self):
        if len(self.get_middle()) != 0: 
            return f'{self.__first} {self.__middle} {self.__last}'
        else:
            return f'{self.__first} {self.__last}'

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
        return f'{self.__street_address}, {self.__city}, {self.__state} {self.__zip_code} ({self.__address_type})'

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
    
class Date:

    def __init__(self, month:str, day:str, year:str) -> None :
        self.__month = month
        self.__day = day
        self.__year = year

    def display(self) -> None : 
        print(f'{self.__month}/{self.__day}/{self.__year}')

    def __str__(self) -> str :
        return f'{self.__month}/{self.__day}/{self.__year}'

    # Getters / Setters

    def get_month(self) -> str : 
        return self.__month

    def get_day(self) -> str : 
        return self.__day

    def get_year(self) -> str : 
        return self.__year

    def set_month(self, new_month:str) -> str : 
        self.__month = new_month

    def set_day(self, new_day:str) -> str : 
        self.__day = new_day

    def set_year(self, new_year:str) -> str : 
        self.__year = new_year

class Semester:

    valid_sems = ['summer', 'fall', 'spring']

    def __init__(self, semester='', year=0):

        if semester.lower() in self.valid_sems:
            self.__semester = semester
        else:
            raise ValueError(f'Error: Invalid Semester Value')
        
        self.__year = year
    
    def set_semester(self, semester):
        if semester.lower() in self.valid_sems:
            self.__semester = semester
        else:
            raise ValueError(f'Error: Invalid Semester Value')
    
    def get_semester(self):
        return self.__semester
    
    def set_year(self, year):
        if isinstance(year, int) and 1900<year<2100:
            self.__year = year
        else:
            print(f'Error: Semester Year Blank')
    
    def get_year(self):
        return self.__year
    
    def display(self):
        print(f'{self.__semester} {self.__year}')

    def __str__(self):
        return f'{self.__semester} {self.__year}'

if __name__ == '__main__':

    # Name ADT Test
    name1 = Name('Pablo', 'Emilio', 'Escobar')
    print(name1)

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

    # Date ADT Test
    date1 = Date('10','16','2025')
    print(date1)

    # Semester ADT Test
    semester1 = Semester('Summer', '2023')
    print(semester1)