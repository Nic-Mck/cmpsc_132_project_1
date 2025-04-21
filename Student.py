# Names: Nick McKenna, Edward Hu
# Class: CMPSC132
# Date of Final Revision: 3-18-2025

# This module defines students in an advisor system as specified

from StudentAttributes import Name, Address, EmailAddress, PhoneNumber, Date, Semester, Course

from linked_list import LinkedList


class Student:

    def __init__(self, name ='', address = '', id_num=0, birthdate='', acceptance_date='',
                 start_semester='', intended_major=''):
        self.__name = name #or Name()
        self.__address = address #or Address()
        self.__id_num = id_num
        self.__email_addresses = [] #or EmailAddress()
        self.__phone_numbers = []  #or PhoneNumber()
        self.__birthdate = birthdate #or Date()
        self.__acceptance_date = acceptance_date #or Date()
        self.__semester = start_semester #or Semester()
        self.__course_list = LinkedList() 
        self.__intended_major = intended_major

    def set_name(self, name) -> int :
        if isinstance(name, (Name,str)):
            self.__name = name
            return 1
        else:
            print(f'Error: Student Name Blank')
            return 0

    def get_name(self):
        return self.__name
    
    def set_address(self, address) -> bool :
        if isinstance(address, (Address, str)):
            self.__address = address
            return True
        else:
            print(f'Error: Student Address Invalid')
            return False

    def get_address(self):
        return self.__address

    def set_id_num(self, id_num):
        if id_num and isinstance(id_num, int):
            self.__id_num = id_num
        else:
            print(f'Error: Student ID Number must be positive integer')

    def get_id_num(self):
        return self.__id_num

    def set_email_addresses(self, email_addresses) -> int:
        if isinstance(email_addresses, (EmailAddress, str)):
            self.__email_addresses = [email_addresses] # Edge case of a single email instead of a list of emails

        if isinstance(email_addresses, list):
            self.__email_addresses = []
            for i in email_addresses:
                if isinstance(i, (EmailAddress,str)):
                    self.__email_addresses.append(i)
                    return 1
                else:
                    print(f'Error: {i} is not a Email Address')
                    return 0
        else:
            print(f'Error: Email Address Invalid')
            return 0

    def get_email_addresses(self):
        return self.__email_addresses
    
    def append_email_address(self, new_email:EmailAddress) -> int : 
        if not isinstance(new_email, (EmailAddress, str)) : 
            raise Exception('Not an Email Address Object')
            return 0

        self.__email_addresses.append(new_email) 
        return 1

    def set_phone_numbers(self, phone_numbers):
        if isinstance(phone_numbers, (PhoneNumber,str)):
            self.__phone_numbers = [phone_numbers] # Edge case of a single number instead of list of nums

        if isinstance(phone_numbers, list):
            self.__phone_numbers = []
            for i in phone_numbers:
                if isinstance(i, (PhoneNumber,str)):
                    self.__phone_numbers.append(i)
                else:
                    print(f'Error: {i} is not a Phone Number')
        else:
            print(f'Error: Invalid Phone Number')

    def get_phone_numbers(self):
        return self.__phone_numbers
    
    def append_phone_number(self, new_phone_number:PhoneNumber) -> int : 
        if not isinstance(new_phone_number, (PhoneNumber,str)) : 
            raise Exception("New Phone Number is not a PhoneNumber Object")
            return 0
        
        self.__phone_numbers.append(new_phone_number)
        return 1

    def set_birthdate(self, birthdate) -> int:
        if isinstance(birthdate, (Date,str)):
            self.__birthdate = birthdate
            return 1
        else:
            print(f'Error: Invalid Date')
            return 0

    def get_birthdate(self):
        return self.__birthdate

    def set_acceptance_date(self, acceptance_date) -> int:
        if isinstance(acceptance_date, (Date,str)):
            self.__acceptance_date = acceptance_date
            return 1
        else:
            print(f'Error: Invalid Date')
            return 0

    def get_acceptance_date(self):
        return self.__acceptance_date

    def set_semester(self, semester) -> int :
        if isinstance(semester, (Semester,str)):
            self.__semester = semester
            return 1
        else:
            print(f'Error: Invalid semester')
            return 0

    def get_semester(self):
        return self.__semester
    
    def set_course_list(self, courses):
        if isinstance(courses, (Course, str)):
            self.__course_list.append_node(courses)
        
        if isinstance(courses, list):
            self.__course_list = LinkedList()
            for i in courses:
                if isinstance(i, (Course, str)):
                    self.__course_list.append_node(i)
                else:
                    print(f'Error: {i} is not a valid Course')
        else:
            print(f'Error: Invalid Course')

    def get_course_list(self):
        return self.__course_list
    
    def append_course_list(self, new_course:Course) -> int:
        if not isinstance(new_course, (Course, str)):
            raise Exception('New Course is not a Course object')
            return 0
        
        self.__course_list.append_node(new_course)
        return 1

    def set_intended_major(self, intended_major) -> int :
        if intended_major:
            self.__intended_major = intended_major
            return 1
        else:
            print(f'Error: Please enter a valid major')
            return 0

    def get_intended_major(self):
        return self.__intended_major

    """def display_data(self):
        email_list = "\n".join(str(e) for e in self.__email_addresses) if self.__email_addresses else "[]"
        phone_list = "\n".join(str(e) for e in self.__phone_numbers) if self.__phone_numbers else "[]"
        #course_list = "\n".join(str(e) for e in self.__course_list) if self.__course_list else "[]"

        print(f'\nStudent Name: {self.get_name()}\nStudent Address: {self.get_address()}\nStudent ID: {self.get_id_num()}\n'
              f'Email Addresses:\n{email_list}\nPhone Numbers: {phone_list}\n'
              f'Birth Date: {self.get_birthdate()}\nAcceptance Date: {self.get_acceptance_date()}\n'
              f'Semester: {self.get_semester()}\nIntended Major: {self.get_intended_major()}\nCourse List:\n{self.__course_list.display()}')"""

    def __str__(self):
        email_list = "\n".join(str(e) for e in self.__email_addresses) if self.__email_addresses else "[]"
        phone_list = "\n".join(str(e) for e in self.__phone_numbers) if self.__phone_numbers else "[]"
        #course_list = "\n".join(str(e) for e in self.__course_list) if self.__course_list else "[]"
        
        return f'\nStudent Name: {self.get_name()}\nStudent Address: {self.get_address()}\nStudent ID: {self.get_id_num()}\n'\
               f'Email Addresses:\n{email_list}\nPhone Numbers: \n{phone_list}\n'\
               f'{"Birth Date: ":<20}' + f'{self.get_birthdate()}'f'\n{"Acceptance Date:":<20}{self.get_acceptance_date()}\n'\
               f'{"Semester: ":<20}' + f'{self.get_semester()}\nIntended Major: {self.get_intended_major()}\nCourse List:\n{self.get_course_list().display()}'

if __name__ == '__main__':

    # Setter & Getter Test
    #s1 = Student('CJ', 479999, '10/20/2003', '10/24/2024',
            #'Fall 2023', 'Mechanical Engineering')

    #print(s1)

    # Email ADT Test
    email1 = EmailAddress('info@tunerdesign.org', 'Business')
    email2 = EmailAddress('sales@tunerdesign.org', 'Marketing')
    s2_emails = [email1, email2]

    s2 = Student('Michael DeSanta', '5066 Portola Ave' ,479998, '10/15/2003', '6/23/23',
                 'Summer 2023', 'Computer Science')
    s2.set_email_addresses(s2_emails)
    #print(s2)

    #Phone ADT Test

    phone1 = PhoneNumber('484-232-2323', 'Cell')
    phone2 = PhoneNumber('1-800-TESTING', 'Business')
    s2_phones = [phone1, phone2]

    s2.set_phone_numbers(s2_phones)
    #print(s2)

    #Address ADT Test

    s2_address = Address('5176 Whispymound Dr', 'Los Santos', 'CA', '97707', 'Residential')
    s2.set_address(s2_address)
    #print(s2)

    #Date ADT Test

    a_date1 = Date('6','24','2023')
    b_date1 = Date('12','24','2004')
    s2.set_acceptance_date(a_date1)
    s2.set_birthdate(b_date1)
    #print(s2)

    #Semester ADT Test

    s2_semester = Semester('Summer', 2023)
    s2.set_semester(s2_semester)
    #print(s2)

    #Name ADT Test

    s2_name = Name('Pablo', 'Emilio', 'Escobar')
    s2.set_name(s2_name)
    #print(s2)

    #Course ADT Test

    course1 = Course('CMPSC132',s2_semester, 'Classroom', 'Current', 'A')
    course2 = Course('MATH141', s2_semester, 'Classroom', 'Current', 'B')
    s2_courselist = []
    s2_courselist.append(course1)
    s2_courselist.append(course2)
    s2.set_course_list(s2_courselist)

    print(s2)