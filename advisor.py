import Student
import linked_list
import node 
from StudentAttributes import *
import datetime
import calendar

# FIXME
# Ad an Advisor
# Edit Advisor Info
# Display Advisor Info 
# Add students to advisee list+
# Delete students from advisee list 

class advisor : 
    def __init__(self, name:str, title:str, department:str):
        self.__name:str = name
        self.__title:str = title
        self.__department:str = department
        self.__advisees:linked_list.LinkedList[Student.Student] = linked_list.LinkedList()

    def add_student(self, new_student:Student.Student) -> None :
        self.__advisees.append_node(new_student)

    def display_advisor(self) -> None : 
         print(
              f'Name: {self.__name}\n'
              f'Title: {self.__title}\n'
              f'Department {self.__department}\n' 
            )

    def set_name(self, new_name:str) -> None : 
        pass
    def set_title(self, new_title:str) -> None : 
        pass
    def set_department(self, new_department:str) -> None :
        pass
    
    def get_name(self) -> str : 
        return self.__name 
    def get_title(self) -> str : 
        return self.__title
    def get_department(self) -> str : 
        return self.__department
    
    def print_main_menu(self) -> None : 
        print(f'\n---{self.__name}---\n'
            '1. Add Student\n'
            '2. Edit Student Data\n'
            '3. Delete Student\n'
            '4. Display Student Data\n'
            '5. Display Advisees\n'
            '6. Back\n'
            )
    
    def edit_student(self) -> None : 
        success:int = 0
        
        print("\n---Edit Student---")
        try:
            id_to_edit:int = int(input("Enter id number of student you wish to edit or -1 to go back: "))
            if id_to_edit < -1:
                 raise ValueError(f'Error: Please enter a valid student ID (must be a positive number)')

        except ValueError:
             print(f'Error: Please enter a valid student ID (must be a positive number)')
             return
        
        # If user wants to go back, return go back signal
        if id_to_edit == -1 : 
            return -1
        
        student = self.__advisees.search(id_to_edit)

        if student is None : 
            print("\nStudent not found, try again")
        else : 
            print(student)
            correct_student:bool = int(input(f'This student was found, is this correct? (1 for yes 0 for no) '))

            if correct_student : 
                continue_editing:int = 1

                while continue_editing != -1 : 
                    self.print_edit_menu()
                    sub_menu_choice:int = int(input("Enter submenu choice or -1 to go back: "))

                    match sub_menu_choice : 
                        case -1 : # Go back
                            continue_editing = -1
                            success = -1
                        case 1 : # Name
                            success = self.edit_student_name(student)
                        case 2 : # Birthdate
                            success = self.edit_student_birthdate(student)
                        case 3 : #Acceptance Date
                            success = self.edit_acceptance_date(student)
                        case 4 : # Semester 
                            success = self.edit_student_semester(student)
                        case 5 : # Intended Major
                            success = self.edit_student_intended_major(student)
                        case 6 : # Add an email address
                            success = self.add_email_address(student)
                        case 7 : # Add a phone number
                            success = self.add_phone_number(student)
                        case 8 : # Edit Address
                            success = self.edit_home_address(student)
                        case _ : # Default Case
                            raise Exception("Invalid submenu choice")
                    
            else : 
                print("Searching for another student with same ID...")

        # If student wasn't found, raise exception
        if success == 0: 
            raise Exception("Student not found")
        
    def print_edit_menu(self) -> None : 
        print(f'\n---Attributes---\n'
            '1. Name\n'
            '2. Birthdate\n'
            '3. Acceptance Date\n'
            '4. Semester\n'
            '5. Intended Major\n'
            '6. Add Email Address\n'
            '7. Add Phone Number\n'
            '8. Edit Home Address\n'
            )
        
    def edit_student_name(self, student:Student) -> int :
        print('\n---Edit Name---')
        while True:
                try:
                    new_first:str = input("Enter new first name : ")
                    if not new_first.isalpha():
                        raise TypeError(f"Error: Please enter a valid first name")
                    if len(new_first) > 0:
                        break
                    else:
                        raise ValueError(f"Error: First Name cannot be blank")
                except ValueError:
                    print(f"Error: First Name cannot be blank")
                except TypeError:
                    print(f"Error: Please enter a valid first name")

        while True:
            try:    
                new_middle:str = input("Enter new middle name : ")
                if new_middle.isalpha() or len(new_middle) == 0:
                    break
                else:
                    raise ValueError(f"Error: Please enter a valid middle name, or press [Enter] to continue if None")
            except ValueError:
                print(f"Error: Please enter a valid middle name, or press [Enter] to continue if None")

        while True:
                try:
                    new_last:str = input("Enter new last name : ")
                    if not new_last.isalpha():
                        raise TypeError(f"Error: Please enter a valid last name")
                    if len(new_last) > 0:
                        break
                    else:
                        raise ValueError(f"Error: Last Name cannot be blank")
                except ValueError:
                    print(f"Error: Last Name cannot be blank")
                except TypeError:
                    print(f"Error: Please enter a valid last name")

        return student.set_name(Name(new_first, new_middle, new_last))

    def edit_student_birthdate(self, student:Student) -> int : 
        print('\n---Edit Birthdate---')
        while True:
            try:
                new_year:int = int(input("Enter new birthdate year : "))
                if new_year < 1000 or new_year > datetime.datetime.now().year:
                    raise ValueError(f'Error: Please enter a valid year')
                else:
                    break
            except ValueError:
                print(f'Error: Please enter a valid year')
        
        while True:
            try:
                new_month:int = int(input("Enter new birthdate month : "))
                if new_month < 1 or new_month > 12:
                    raise ValueError(f"Error: Please enter a valid month [1-12] for {new_year}")
                else:
                    break
            except ValueError:
                print(f"Error: Please enter a valid month [1-12] for {new_year}")

        while True:
            try:
                new_day:int = int(input("Enter new birthdate day : "))
                last_day_of_month = calendar.monthrange(new_year, new_month)[1]
                month_to_str = calendar.month_name[new_month]
                if new_day < 1 or new_day > last_day_of_month:
                    raise ValueError(f"Error: Please enter a valid day [1-{last_day_of_month}] for {month_to_str}, {new_year}")
                else:
                    break
            except ValueError:
                print(f"Error: Please enter a valid day [1-{last_day_of_month}] for {month_to_str}, {new_year}")

        return student.set_birthdate(Date(new_month, new_day, new_year))

    def edit_acceptance_date(self, student:Student) -> int : 
        print('\n---Edit Acceptance Date---')
        while True:
            try:
                new_year:int = int(input("Enter new birthdate year : "))
                if new_year < 1000 or new_year > datetime.datetime.now().year:
                    raise ValueError(f'Error: Please enter a valid year')
                else:
                    break
            except ValueError:
                print(f'Error: Please enter a valid year')
        
        while True:
            try:
                new_month:int = int(input("Enter new birthdate month : "))
                if new_month < 1 or new_month > 12:
                    raise ValueError(f"Error: Please enter a valid month [1-12] for {new_year}")
                else:
                    break
            except ValueError:
                print(f"Error: Please enter a valid month [1-12] for {new_year}")

        while True:
            try:
                new_day:int = int(input("Enter new birthdate day : "))
                last_day_of_month = calendar.monthrange(new_year, new_month)[1]
                month_to_str = calendar.month_name[new_month]
                if new_day < 1 or new_day > last_day_of_month:
                    raise ValueError(f"Error: Please enter a valid day [1-{last_day_of_month}] for {month_to_str}, {new_year}")
                else:
                    break
            except ValueError:
                print(f"Error: Please enter a valid day [1-{last_day_of_month}] for {month_to_str}, {new_year}")

        return student.set_acceptance_date(Date(new_month, new_day, new_year))

    def edit_student_semester(self, student:Student) -> int : 
        print('\n---Edit Semester---')
        while True:
                new:str = input("Enter new semester (Fall/Spring/Summer): ")
                if len(new) > 0:
                    break
                else:
                    print("Error: Semester cannot be blank")

        # Revise for int data type
        while True:
                try:
                    year:int = int(input("Enter the year : "))
                    if 1900 < year < 2100:
                        break
                    else:
                        print("Error: Semester year must be between 1900 and 2100")
                except ValueError:
                    print("Error: Semester year cannot be blank")

        return student.set_semester(Semester(new, year))

    def edit_student_intended_major(self, student:Student) -> int :
        while True:
                print("\n---Edit Intended Major---")
                new:str = input("Enter new major : ")
                if len(new) > 0:
                    break
                else:
                    print("Error: Intended major cannot be blank")

        return student.set_intended_major(new)

    def add_email_address(self, student:Student) -> int : 
        print('\n---Add Email Address---')
        while True:
                address:str = input("Enter new email address : ")
                if len(address) > 0:
                    break
                else:
                    print("Error: Email address blank")

        while True:
                add_type:str = input("Enter email address type : ")
                if len(add_type) > 0:
                    break
                else:
                    print("Error: Email type blank")
        
        new_email = EmailAddress(address, add_type)

        # Attempt to append email and return True or False for Success or Failure
        return student.append_email_address(new_email)

    def add_phone_number(self, student:Student) -> int : 
        print('\n---Add Phone Number---')
        while True:
                new_number:str = input("Enter new phone number : ")
                if len(new_number) > 0:
                    break
                else:
                    print("Error: Phone number blank")

        while True:
                new_number_type:str = input("Enter phone number type (Business, Personal, Etc.) : ")
                if len(new_number_type) > 0:
                    break
                else:
                    print("Error: Phone type blank")
        
        new_phone_number:PhoneNumber = PhoneNumber(new_number, new_number_type)
        
        # Attempt to append phone number and return True or False for Success or Failure
        return student.append_phone_number(new_phone_number)

    def edit_home_address(self, student:Student) -> int : 
        print("\n---Edit Home Address---")
        new_street_adr:str = str(input("Enter Street Address : "))
        while len(new_street_adr) <= 0 : 
            print("Invalid, address cannot be blank")
            new_street_adr = str(input("Enter Street Address : "))

        new_city:str = str(input("Enter new city : "))
        while len(new_city) <= 0 :
            print("Invalid, City Name Cannot be blank")
            new_city = str(input("Enter new city : "))
        
        new_state:str = str(input("Enter new state : "))
        while len(new_state) <= 0 :
            print("Invalid, State cannot be blank")
            new_state:str = str(input("Enter new state : "))

        new_zipcode:str = str(input("Enter new zipcode : "))
        while len(new_zipcode) <= 0 :
            print("Invalid, zipcode cannot be blank")
            new_zipcode:str = str(input("Enter new zipcode : "))

        new_addr_type:str = str(input("Enter address type : "))
        while len(new_addr_type) <= 0 : 
            print("Invalid, address type cannot be blank")
            new_addr_type:str = str(input("Enter address type : "))

        return student.set_address(Address(new_street_adr, new_city, new_state, new_zipcode, new_addr_type))

    def construct_student(self) -> Student.Student : 
        print('\n---Add Student---')
        """try : 
            while True:
                name:str = str(input("Enter student's name: "))
                if len(name) > 0:
                    break
                else:
                    print("Invalid input. Please enter a valid student Name.")"""
        
        try : 
            while True:
                try:
                    first_name:str = str(input("Enter student's first name: "))
                    if not first_name.isalpha():
                         raise TypeError("Error: Please enter a valid student Name.")
                    if len(first_name) > 0:
                        break
                    else:
                        raise ValueError("Error: Please enter a valid student Name.")
                except ValueError:
                     print("Error: Please enter a valid student Name.")
                except TypeError:
                     print("Error: Please enter a valid student Name.")
            
            while True:
                try:
                    middle_name:str = str(input("Enter student's middle name: "))
                    if middle_name.isalpha() or len(middle_name) == 0:
                         break
                    else:
                         raise TypeError(f"Error: Please enter a valid middle name")
                #REVISEME Does not take middle names such as van de pol or Barrett-Saxon
                except TypeError:
                     print(f"Error: Please enter a valid middle name (if multiple, enter as one with each capitalized)")
            
            while True:
                try:
                    last_name:str = str(input("Enter student's last name: "))
                    if not last_name.isalpha():
                         raise TypeError("Error: Please enter a valid last Name.")
                    if len(last_name) > 0:
                        break
                    else:
                        raise ValueError("Error: Please enter a valid last Name.")
                except ValueError:
                     print("Error: Please enter a valid last Name.")
                except TypeError:
                     print("Error: Please enter a valid last Name.")

            name = str(Name(first_name, middle_name, last_name))

            # Revise for Int data type
            unique_id_number = False
            while not unique_id_number:
                try:
                    id_num:int = int(input("Enter student's id number: "))
                    if id_num < 0:
                         raise ValueError("Error: Please enter a valid student ID number (must be positive number)")

                    if not self.__advisees.search(id_num) : 
                        unique_id_number = True 
                    else : 
                        print("ID Number already in use, try again")

                except ValueError:
                    print("Error: Please enter a valid student ID number (must be positive number)")
            
            print("Enter student's birthdate: ")
            while True:
                try:
                    year:int = int(input("Year: "))
                    if year < 1000 or year > datetime.datetime.now().year:
                        raise ValueError(f"Error: Please enter a valid year")
                    else:
                        break
                except ValueError:
                     print(f"Error: Please enter a valid year")

            while True:
                try:
                    month:int = int(input("Month: "))
                    if month < 1 or month > 12:
                        raise ValueError(f"Error: Please enter a valid month")
                    else:
                        break
                except ValueError:
                    print(f'Error: Please enter a valid month for {year}')

            while True:
                try:
                    day:int = int(input("Day: "))
                    last_day_of_month = calendar.monthrange(year, month)[1]
                    month_to_str = calendar.month_name[month]
                    if day < 1 or day > last_day_of_month:
                        raise ValueError(f"Error: Please enter a valid day [1-{last_day_of_month}] for {month_to_str}, {year}")
                    else:
                        break
                except ValueError:
                    print(f"Error: Please enter a valid day [1-{last_day_of_month}] for {month_to_str}, {year}")
            
            birthdate = str(Date(month, day, year))
            
            print("Enter student's acceptance date: ")
            while True:
                try:
                    year2:int = int(input("Year: "))
                    if year2 < 1900 or year2 > datetime.datetime.now().year:
                        raise ValueError(f"Error: Please enter a valid year")
                    else:
                        break
                except ValueError:
                     print(f"Error: Please enter a valid year")
            
            while True:
                try:
                    month2:int = int(input("Month: "))
                    if month2 < 1 or month2 > 12:
                        raise ValueError(f"Error: Please enter a valid month")
                    else:
                        break
                except ValueError:
                    print(f'Error: Please enter a valid month for {year2}')

            while True:
                try:
                    day2:int = int(input("Day: "))
                    last_day_of_month = calendar.monthrange(year2, month2)[1]
                    month_to_str = calendar.month_name[month2]
                    if day2 < 1 or day2 > last_day_of_month:
                        raise ValueError(f"Error: Please enter a valid day [1-{last_day_of_month}] for {month_to_str}, {year2}")
                    else:
                        break
                except ValueError:
                    print(f"Error: Please enter a valid day [1-{last_day_of_month}] for {month_to_str}, {year}")

            acceptance_date = str(Date(month2,day2,year2))

            print("Enter student's start semester (semester, year): ")
            while True:
                valid_sems = ['summer', 'fall', 'spring']
                try:
                    semester:str = str(input("Semester: "))
                    if semester.lower() in valid_sems:
                        break
                    else:
                        raise ValueError(f'Error: Please enter a valid start semester (summer/fall/spring)')
                except ValueError:
                    print(f'Error: Please enter a valid start semester (summer/fall/spring)')

            while True:
                try:
                    semester_year:int = int(input("Year: "))
                    if 1900 <= semester_year <= datetime.datetime.now().year:
                        break
                    else:
                        raise ValueError(f"Error: Please enter a valid year for {semester} Semester")
                except ValueError:
                    print(f"Error: Please enter a valid year for {semester} Semester")

            start_semester = str(Semester(semester, semester_year))

            while True:
                try:
                    intended_major:str = str(input("Enter student's intended major: "))
                    if not isinstance(intended_major, str):
                        raise TypeError(f"Error: Please enter a valid major.")
                    if len(intended_major) > 0:
                        break
                    else:
                        raise ValueError(f"Error: Please enter a valid major.")
                except ValueError:
                    print(f"Error: Please enter a valid major.")
                except TypeError:
                    print(f"Error: Please enter a valid major.")

            test_blank_list = [name, birthdate, acceptance_date, semester, intended_major]

            for case in test_blank_list : 
                if len(case.strip()) == 0 :
                    print(f'Error, attribute {case} cannot be blank')
                    return None

        # Catch errors and print to user to prevent program crash
        except Exception as e : 
            print(e)
        try : 
            new_student:Student.Student = Student.Student(name, '', id_num, birthdate, acceptance_date, start_semester, intended_major)
            print(f'\n New Student ({new_student.get_name()}) Added Successfully!')
            return new_student
        except Exception as e : # No exceptions are setup atm, just returning None
            return None

    def delete_student(self) -> int : 
        while True:
            try:
                print('\n---Delete Student---')
                id_to_del:int = int(input("Enter id number of student you want to delete or -1 to go back : "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid student ID to delete.")

        if id_to_del == -1 : # Go back a menu indicator
            return 0
        
        student = self.__advisees.search(id_to_del)
        if student is not None : 
                student.display_data()
                do_delete:bool = int(input("\nIs this the correct student to delete? (1 for yes, 0 for no) : "))

                if do_delete : 
                    #FIXME
                    # Call delete student(student) on advisor class here
                    self.__advisees.remove_data(student)
                    print("Student successfully deleted\n")
                    success = True
                    return 1
                else : 
                    print("\nWrong student indicated, searching for another student with same ID...")

        print("Failed to delete, student not found")
        return -1

    def display_student(self) -> int : 
        print('\n---Display Student---')
        while True:
            try:
                id_to_display:int = int(input("Enter id number of student to display or -1 to go back : "))
                if id_to_display < -1:
                     raise ValueError("Error: Please enter a valid student ID to display (must be positive number).")
                break
            except ValueError:
                print("Error: Please enter a valid student ID to display (must be positive number).")

        # If user wishes to go back, return 0 to indicate this to main loop
        if id_to_display == -1 : 
            return 0 
        
        student = self.__advisees.search(id_to_display)
        if student is None : 
            print(f'Error: Student ID not found in system')
            return -1
        else : 
             print(student)
             return 1

    def display_advisees(self) -> None : 
        self.__advisees.display()

    def append_student(self, stud:Student.Student) -> None : 
         self.__advisees.append_node(stud)