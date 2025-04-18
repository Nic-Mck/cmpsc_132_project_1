import Student
import linked_list
import node 
from StudentAttributes import *

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
        print(f'\n1. Add Student\n'
            '2. Edit Student Data\n'
            '3. Delete Student\n'
            '4. Display Student Data\n'
            '5. Exit\n'
            )
    
    def edit_student(self, students) -> None : 
        success:int = 0
        
        id_to_edit:int = int(input("Enter id number of student you wish to edit or -1 to go back: "))
        
        # If user wants to go back, return go back signal
        if id_to_edit == -1 : 
            return -1

        for student in students : 
            if student.get_id_num() == id_to_edit : 
                student.display_data()
                correct_student:int = int(input("Is this the correct student? (1 for yes, 0 for no) : "))

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
                        
                    break # Exit loop as student was found
                else : 
                    print("Searching for another student with same ID...")

        # If student wasn't found, raise exception
        if success == 0: 
            raise Exception("Student not found")
        
    def print_edit_menu(self) -> None : 
        print(f'\nAttributes:\n'
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
        while True:
                new_first:str = input("Enter new first name : ")
                if len(new_first) > 0:
                    break
                else:
                    print("Error: First Name cannot be blank")

        new_middle:str = input("Enter new middle name : ")

        while True:
                new_last:str = input("Enter new last name : ")
                if len(new_last) > 0:
                    break
                else:
                    print("Error: Last Name cannot be blank")

        return student.set_name(Name(new_first, new_middle, new_last))

    def edit_student_birthdate(self, student:Student) -> int : 

        while True:
                new_day:str = input("Enter new birthdate day : ")
                if len(new_day) > 0:
                    break
                else:
                    print("Error: Day cannot be blank")

        while True:
                new_month:str = input("Enter new birthdate month : ")
                if len(new_month) > 0:
                    break
                else:
                    print("Error: Month cannot be blank")

        while True:
                new_year:str = input("Enter new birthdate year : ")
                if len(new_year) > 0:
                    break
                else:
                    print("Error: Year cannot be blank")

        return student.set_birthdate(Date(new_month, new_day, new_year))

    def edit_acceptance_date(self, student:Student) -> int : 
        while True:
                new_day:str = input("Enter new birthdate day : ")
                if len(new_day) > 0:
                    break
                else:
                    print("Error: Day cannot be blank")

        while True:
                new_month:str = input("Enter new birthdate month : ")
                if len(new_month) > 0:
                    break
                else:
                    print("Error: Month cannot be blank")

        while True:
                new_year:str = input("Enter new birthdate year : ")
                if len(new_year) > 0:
                    break
                else:
                    print("Error: Year cannot be blank")

        return student.set_acceptance_date(Date(new_month, new_day, new_year))

    def edit_student_semester(self, student:Student) -> int : 
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
                new:str = input("Enter new major : ")
                if len(new) > 0:
                    break
                else:
                    print("Error: Intended major cannot be blank")

        return student.set_intended_major(new)

    def add_email_address(self, student:Student) -> int : 
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

    def construct_student(self, students) -> Student.Student : 
        try : 
            while True:
                name:str = str(input("Enter student's name: "))
                if len(name) > 0:
                    break
                else:
                    print("Invalid input. Please enter a valid student Name.")

            # Revise for Int data type
            unique_id_number = False
            while not unique_id_number:
                broken = False
                try:
                    id_num:int = int(input("Enter student's id number: "))
                    for s in students :
                        if id_num == s.get_id_num() : 
                            print("Invalid, id num already in use")
                            broken = True 
                            break
                    
                    if not broken : 
                        unique_id_number = True

                except ValueError:
                    print("Invalid input. Please enter a valid student ID number")
            
            while True:
                    birthdate:str = str(input("Enter students birthdate (mm/dd/yyyy): "))
                    if len(birthdate) > 0:
                        break
                    else:
                        print("Invalid input. Please enter a valid date.")
            
            while True:
                    acceptance_date:str = str(input("Enter student's acceptance date (mm/dd/yyyy): "))
                    if len(acceptance_date) > 0:
                        break
                    else:
                        print("Invalid input. Please enter a valid date.")

            while True:
                    semester:str = str(input("Enter current sememster: "))
                    if len(semester) > 0:
                        break
                    else:
                        print("Invalid input. Please enter a valid semester.")

            while True:
                    intended_major:str = str(input("Enter student's intended major: "))
                    if len(intended_major) > 0:
                        break
                    else:
                        print("Invalid input. Please enter a valid major.")

            test_blank_list = [name, birthdate, acceptance_date, semester, intended_major]

            for case in test_blank_list : 
                if len(case.strip()) == 0 :
                    print(f'Error, attribute {case} cannot be blank')
                    return None

        # Catch errors and print to user to prevent program crash
        except Exception as e : 
            print(e)

        try : 
            # FIXME
            # Call add_student on advisor class here
            new_student:Student.Student = Student.Student(name, '', id_num, birthdate, acceptance_date, semester, intended_major)
            return new_student
        except Exception as e : # No exceptions are setup atm, just returning None
            return None

    def delete_student(self, students) -> int : 
        while True:
            try:
                id_to_del:int = int(input("Enter id number of student you want to delete or -1 to go back : "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid student ID to delete.")

        if id_to_del == -1 : # Go back a menu indicator
            return 0
        
        # Find student with matching ID and delete from students array
        for student in students : 
            if student.get_id_num() == id_to_del : 
                student.display_data()
                do_delete:bool = int(input("\nIs this the correct student to delete? (1 for yes, 0 for no) : "))

                if do_delete : 
                    #FIXME
                    # Call delete student(student) on advisor class here
                    students.remove(student) 
                    print("Student successfully deleted\n")
                    success = True
                    return 1
                else : 
                    print("\nWrong student indicated, searching for another student with same ID...")
                    continue

        print("Failed to delete, student not found")
        return -1

    def display_student(self, students) -> int : 
        while True:
            try:
                id_to_display:int = int(input("Enter id number of student to display or -1 to go back : "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid student ID to display.")

        # If user wishes to go back, return 0 to indicate this to main loop
        if id_to_display == -1 : 
            return 0 
        
        for student in students : 
            if student.get_id_num() == id_to_display : 
                print(student)
                return 1
            
        print("Student not found.")
