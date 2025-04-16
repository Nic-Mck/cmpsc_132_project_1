# Names: Nick McKenna, Edward Hu
# Class: CMPSC132
# Date of Final Revision: 3-18-2025

# This module defines attribute ADTs for the Student class

class Name:

    def __init__(self, first='', middle='', last=''):
        try:
            if not isinstance(first, str):
                raise TypeError(f'Error: Please enter a valid first name')
            if first:
                self.__first = first
            else:
                raise ValueError(f'Error: First Name Blank')
        except ValueError as e:
            print(f'Error: First Name Blank')
            self.__first = '(First)'
        except TypeError as e:
            print(f'Error: Please enter a valid first name')
            self.__first = '(First)'

        self.__middle = middle

        try:
            if not isinstance(last, str):
                raise TypeError(f'Error: Please enter a valid last name')
            if last:
                self.__last = last
            else:
                raise ValueError(f'Error: Last Name Blank')
        except ValueError as e:
            print(f'Error: Last Name Blank')
            self.__last = '(Last)'
        except TypeError as e:
            print(f'Error: Please enter a valid last name')
            self.__last = '(Last)'

    def set_first(self, first):
        if not isinstance(first, str):
            raise TypeError(f'Error: Please enter a valid first name')
        if first:
            self.__first = first
        else:
            raise ValueError(f'Error: First Name Blank')

    def get_first(self):
        return self.__first

    def set_middle(self, middle):
        self.__middle = middle      

    def get_middle(self):
        return self.__middle
    
    def set_last(self, last):
        if not isinstance(last, str):
            raise TypeError(f'Error: Please enter a valid last name')
        if last:
            self.__last = last
        else:
            raise ValueError(f'Error: Last Name Blank')

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
        if street_address:
            self.__street_address = street_address
        else:
            raise ValueError(f'Error: Street Address Blank')

    def get_street_address(self):
        return self.__street_address

    def set_city(self, city):
        if city:
            self.__city = city
        else:
            raise ValueError(f'Error: City Blank')

    def get_city(self):
        return self.__city

    def set_state(self, state):
        if state:
            self.__state = state
        else:
            raise ValueError(f'Error: State Blank')

    def get_state(self):
        return self.__state

    def set_zip_code(self, zip_code):
        if zip_code:
            self.__zip_code = zip_code
        else:
            raise ValueError(f'Error: Zip Code Blank')

    def get_zip_code(self):
        return self.__zip_code

    def set_address_type(self, address_type):
        if address_type:
            self.__address_type = address_type
        else:
            raise ValueError(f'Error: Address Type Blank')

    def display(self):
        print(f'{self.__street_address}, {self.__city}, {self.__state} {self.__zip_code}')

    def __str__(self):
        return f'{self.__street_address}, {self.__city}, {self.__state} {self.__zip_code} ({self.__address_type})'

class EmailAddress:

    def  __init__(self, address='', email_type=''):
        try:
            if not isinstance(address, str):
                raise TypeError(f'Error: Please enter a valid email address')
            if address:
                self.__address = address
            else:
                raise ValueError(f'Error: Email Address Blank')
        except ValueError as e:
            print(f'Error: Email Address Blank')
            self.__address = 'example@domain.com'
        except TypeError as e:
            print(f'Error: Please enter a valid email address')
            self.__address = 'example@domain.com'
        
        try:
            if not isinstance(email_type, str):
                raise TypeError(f'Error: Please enter a valid email address')
            if email_type:
                self.__email_type = email_type
            else:
                raise ValueError(f'Error: Email Type Blank')
        except ValueError as e:
            print(f'Error: Email Type Blank')
            self.__email_type = 'Email Type'
        except TypeError as e:
            print(f'Error: Please enter a valid email address type (ex. Personal, Work, Business)')
            self.__email_type = 'Email Type'

    def set_address(self, address):
        if not isinstance(address, str):
            raise TypeError(f'Error: Please enter a valid email address')
        if address:
            self.__address = address
        else:
            raise ValueError(f'Error: Email Address Blank')

    def get_address(self):
        return self.__address

    def set_email_type(self, email_type):
        if not isinstance(email_type, str):
            raise TypeError(f'Error: Please enter a valid email address type (ex. Personal, Work, Business)')
        if email_type:
            self.__email_type = email_type
        else:
            raise ValueError(f'Error: Email Type Blank')

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
        if phone_number:
            self.__phone_number = phone_number
        else:
            raise ValueError(f'Error: Phone Number Blank')

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_type(self, phone_type):
        if phone_type:
            self.__phone_type = phone_type
        else:
            raise ValueError(f'Error: Phone Type Blank')

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
        
        try:
            self.__year = int(year)
            raise ValueError("Invalid input, enter an integer")
        except Exception as e :
            print(f'#Error: Please enter a valid semester year [1900-2100] ')
            #FIXME
            self.__year = "Invalid Input"

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
            raise ValueError(f'Error: Semester Year Invalid')
    
    def get_year(self):
        return self.__year
    
    def display(self):
        print(f'{self.__semester} {self.__year}')

    def __str__(self):
        return f'{self.__semester} {self.__year}'
    
class Course:

    valid_inst_methods = ['classroom', 'hybrid', 'remote']
    valid_status = ['completed', 'dropped', 'current']
    valid_grades = ['a','b','c','d','f','n/a']

    def __init__(self, course_num='', semester=Semester, inst_method='', status='', grade=''):
        
        self.__course_num = course_num
        self.__semester = semester

        if inst_method.lower() in self.valid_inst_methods:
            self.__inst_method = inst_method
        else:
            raise ValueError(f'Error: Please enter a valid course instruction method')
        
        if status.lower() in self.valid_status:
            self.__status = status
        else:
            raise ValueError(f'Error: Please enter a valid course status')
        
        if grade.lower() in self.valid_grades:
            self.__grade = grade
        else:
            raise ValueError(f'Error: Please enter a valid course grade')

    # Note: Optimize this setter to take proper input and format it (eg. CMPSC 132)
    def set_course_num(self, course_num):
        if course_num:
            self.__course_num = course_num
        else:
            raise ValueError(f'Error: Course Number Blank')

    def get_course_num(self):
        return self.__course_num
    
    def set_semester(self, semester):
        if isinstance(semester, Semester):
            self.__semester = semester 
        else:
            raise ValueError(f'Error: Please enter a valid semester')

    def get_semester(self):
        return self.__semester
    
    def set_inst_method(self, inst_method):
        if inst_method.lower() in self.valid_inst_methods:
            self.__inst_method = inst_method
        else:
            raise ValueError(f'Error: Please enter a valid course instruction method')
        
    def get_inst_method(self):
        return self.__inst_method
    
    def set_status(self, status):
        if status.lower() in self.valid_status:
            self.__status = status
        else:
            raise ValueError(f'Error: Please enter a valid course status')
        
    def get_status(self):
        return self.__status
    
    def set_grade(self, grade):
        if grade.lower() in self.valid_grades:
            self.__grade = grade
        else:
            raise ValueError(f'Error: Please enter a valid course grade')
        
    def get_grade(self):
        return self.__grade
    
    # Note: Optimize print & display outputs for this Class
    def display(self):
        print(f'Course ID: {self.__course_num}\nSemester Taken: {self.__semester}\nInstruction Method: {self.__inst_method}\nStatus: {self.__status}\nGrade: {self.__grade.upper()}')

    def __str__(self):
        return f'Course ID: {self.__course_num}\nSemester Taken: {self.__semester}\nInstruction Method: {self.__inst_method}\nStatus: {self.__status}\nGrade: {self.__grade.upper()}'


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
    semester1 = Semester('Summer', 2023)
    print(semester1)

    # Course ADT Test
    course1 = Course('CMPSC 132', semester1, 'Classroom', 'Current', 'a')
    print(course1)