import Student
import linked_list
import node 
from StudentAttributes import *
import datetime
import calendar

# Add an Advisor
# Edit Advisor Info
# Display Advisor Info 
# Add students to advisee list+
# Delete students from advisee list 

class advisor : 

    valid_titles = ['admin', 'advisor', 'professor', 'associate professor', 'assistant professor', 'dr.',
                    'teaching assistant', 'learning assistant', 'doctor', 'researcher', 'lecturer', 'instructor',
                    'ta','la']

    def __init__(self, name:str, title:str, department:str):
        self.__name:str = name
        self.__title:str = title
        self.__department:str = department
        self.__advisees:linked_list.LinkedList[Student.Student] = linked_list.LinkedList()

    def add_student(self, new_student:Student.Student) -> None :
        self.__advisees.append_node(new_student)

    def display_advisor(self) -> None : 
         print(
              f'    Name: {self.__name}\n'
              f'    Title: {self.__title}\n'
              f'    Department: {self.__department}\n' 
            )
         
    def __str__(self) -> str:
        return(
              f'    Name: {self.__name}\n'
              f'    Title: {self.__title}\n'
              f'    Department: {self.__department}\n' 
            )

    def set_name(self, new_name:str) -> None : 
        self.__name = new_name
    def set_title(self, new_title:str) -> None : 
        new_title = new_title.strip().lower()
        if new_title in advisor.valid_titles:
            self.__title = new_title
        else:
            print(f"Error: Invalid Title for Advisor")
    def set_department(self, new_department:str) -> None :
        self.__department = new_department
    
    def get_name(self) -> str : 
        return self.__name 
    def get_title(self) -> str : 
        return self.__title
    def get_department(self) -> str : 
        return self.__department
    
    def print_main_menu(self) -> None : 
        print(f'\n-----Advisors Student Menu: {self.__name}-----\n'
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
            id_to_edit:int = int(input("Enter ID number of student you wish to edit or -1 to go back: "))
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
            
            while True:
                try:
                    user_input = input(f'\nThis student was found, is this correct? [1-Yes, 0-No]: ').strip()
                    if user_input == "":
                        raise ValueError("User Input Blank")
                    if user_input not in ['0','1']:
                        raise ValueError("User Input Invalid")
                    correct_student: bool = bool(int(user_input))
                    break
                except ValueError as e:
                    print(f"\nError: {e}")

            if correct_student : 
                continue_editing:int = 1

                while continue_editing != -1 : 
                    self.print_edit_menu()
                    #sub_menu_choice:int = int(input("Enter submenu choice or -1 to go back: "))

                    try:
                        sub_menu_choice = input("Enter submenu choice or -1 to go back: ").strip()
                        if sub_menu_choice == "":
                            raise ValueError("Input cannot be blank")
                        if not sub_menu_choice.lstrip("-").isdigit():
                            raise ValueError("Please enter a valid menu option [1-9]")
                        sub_menu_choice = int(sub_menu_choice)
                    except ValueError as e:
                        print(f'\nError: {e}')
                        continue

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
                        case 9 : # Edit Course List
                            success = self.edit_course_list(student)
                        case _ : # Default Case
                            raise Exception("Invalid Submenu Choice")
                    
            else : 
                print("Searching for another student with same ID...")

        # If student wasn't found, raise exception
        if success == 0: 
            raise Exception("Student not found in your Advisee List")
        
    def print_edit_menu(self) -> None : 
        print(f'\n---Attributes---\n'
            '1. Edit Name\n'
            '2. Edit Birthdate\n'
            '3. Edit Acceptance Date\n'
            '4. Edit Semester\n'
            '5. Edit Intended Major\n'
            '6. Edit Email Address(s)\n'
            '7. Edit Phone Number(s)\n'
            '8. Edit Home Address\n'
            '9. Edit Course List\n'
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
            valid_sems = ['summer', 'fall', 'spring']
            try:
                new:str = input("Enter new semester (Fall/Spring/Summer): ")
                if new.lower() in valid_sems:
                    break
                else:
                    raise ValueError(f'Error: Please enter a valid start semester (summer/fall/spring)')
            except ValueError:
                print(f'Error: Please enter a valid start semester (summer/fall/spring)')

        while True:
                try:
                    year:int = int(input("Enter the year : "))
                    if 1900 <= year <= datetime.datetime.now().year:
                        break
                    else:
                        raise ValueError(f"Error: Please enter a valid year for {new} Semester")
                except ValueError:
                    print(f"Error: Please enter a valid year for {new} Semester")

        return student.set_semester(Semester(new, year))

    def edit_student_intended_major(self, student:Student) -> int :
        print("\n---Edit Intended Major---")
        while True:
            try:
                new:str = input("Enter new major : ")
                if not isinstance(new, str):
                    raise TypeError(f"Error: Please enter a valid intended major (e.g. Computer Science, Biology etc.)")
                if len(new) > 0:
                    break
                else:
                    raise ValueError(f"Error: Please enter a valid intended major (e.g. Computer Science, Biology etc.)")
            except ValueError:
                print(f"Error: Please enter a valid intended major (e.g. Computer Science, Biology etc.)")
            except TypeError:
                print(f"Error: Please enter a valid intended major (e.g. Computer Science, Biology etc.)")

        return student.set_intended_major(new)

    def add_email_address(self, student:Student) -> int : 
        while True:
            print('\n---Edit Email Addresses---')
            print(f"1. Add Email\n"
                   "2. Remove Email\n"
                   "3. Go Back\n")
            """try:
                user_choice = int(input("Enter your choice or -1 to go back: "))
            except ValueError:
                print(f'\nError: Please enter a valid choice')"""
            
            try:
                user_choice = input("Enter your choice or -1 to go back: ").strip()
                if user_choice == "":
                    raise ValueError("Input cannot be blank")
                if not user_choice.lstrip("-").isdigit():
                            raise ValueError("Please enter a valid menu option [1-3]")
                user_choice = int(user_choice)
            except ValueError as e:
                print(f'\nError: {e}')
                continue
                
            if user_choice == -1:
                return -1
            
            elif user_choice == 1:
                while True:
                    while True:
                        try:
                            address:str = input("Enter new email address : ")
                            if len(address) > 0:
                                break
                            else:
                                raise ValueError(f"Error: Email Address Blank")
                        except ValueError:
                            print(f"Error: Email Address Blank")

                    while True:
                        try:
                            add_type:str = input("Enter email address type : ")
                            if len(add_type) > 0:
                                break
                            else:
                                raise ValueError(f"Error: Email type blank")
                        except ValueError:
                            print (f"Error: Email type blank")
                    
                    new_email = EmailAddress(address, add_type)

                    # Attempt to append email and return True or False for Success or Failure
                    student.append_email_address(new_email)
                    print(f"\nThe following email has been added successfully: {new_email}")

                    try:
                        add_another = int(input(f"\nAdd another email to list? [1-Yes, 0-No]: "))
                        if add_another != 1:
                            break
                    except Exception:
                        print(f"\nError: Invalid Input, returning to menu")
                        break
            
            elif user_choice == 2:
                while True:
                        while True:
                            try:
                                removed_email = input(f"Please enter email to be removed: ").lower().strip()
                                if len(removed_email) > 0:
                                    break
                                else:
                                    raise ValueError(f"\nError: User input blank")
                            except ValueError:
                                print(f"\nError: User input blank")

                        confirm_remove = int(input(f"\nConfirm deletion of {removed_email} [1-Yes, 0-No]"))  
                        if confirm_remove == 1:      
                            result = student.remove_email_address(removed_email)
                            print(f"{removed_email} has been removed successfully" if result else f"{removed_email} not found in list")
                        else:
                            print("\nDeletion cancelled")

                        try:
                            remove_another = int(input(f"\nRemove another email from list? [1-Yes, 0-No]: "))
                            if remove_another != 1:
                                break
                        except Exception:
                            print(f"\nError: Invalid Input, returning to menu")
                            break
                        
            elif user_choice == 3:
                break

            else:
                print(f"\nError: Please enter a valid menu option [1-3]")

    def add_phone_number(self, student:Student) -> int : 
        while True:
            print('\n---Edit Phone Numbers---')
            print(f"1. Add Phone Number\n"
                   "2. Remove Phone Number\n"
                   "3. Go Back\n")

            try:
                user_choice = input("Enter your choice or -1 to go back: ").strip()
                if user_choice == "":
                    raise ValueError("Input cannot be blank")
                if not user_choice.lstrip("-").isdigit():
                            raise ValueError("Please enter a valid menu option [1-3]")
                user_choice = int(user_choice)
            except ValueError as e:
                print(f'\nError: {e}')
                continue

            if user_choice == -1:
                return -1
            
            elif user_choice == 1:
                while True:
                    while True:
                        try:
                            new_number:str = input("Enter new phone number : ")
                            if len(new_number) > 0:
                                break
                            else:
                                raise ValueError("Error: Phone number blank")
                        except ValueError:
                            print("Error: Phone number blank")

                    while True:
                        try:
                            new_number_type:str = input("Enter phone number type (Business, Personal, Etc.) : ")
                            if len(new_number_type) > 0:
                                break
                            else:
                                raise ValueError("Error: Phone type blank")
                        except ValueError:
                            print("Error: Phone type blank")
                    
                    new_phone_number:PhoneNumber = PhoneNumber(new_number, new_number_type)
                    
                    # Attempt to append phone number and return True or False for Success or Failure
                    student.append_phone_number(new_phone_number)
                    print(f"\nThe following phone number has been added successfully: {new_phone_number}")

                    try:
                        add_another = int(input(f"\nAdd another phone number to list? [1-Yes, 0-No]: "))
                        if add_another != 1:
                            break
                    except Exception:
                        print(f"\nError: Invalid input, returning to menu")
                        break

            elif user_choice == 2:
                 while True:
                        while True:
                            try:
                                removed_number = input(f"Please enter phone number to be removed: ").lower().strip()
                                if len(removed_number) > 0:
                                    break
                                else:
                                    raise ValueError(f"\nError: User input blank")
                            except ValueError:
                                print(f"\nError: User input blank")

                        confirm_remove = ''

                        while len(confirm_remove) <= 0 and confirm_remove != '-1' : 
                            confirm_remove = str(input(f"\nConfirm deletion of {removed_number} [1-Yes, 0-No]"))  

                            if len(removed_number) <= 0 :
                                print("Invalid input")
                            elif confirm_remove == '-1' : 
                                return -1
                            
                        if confirm_remove == '1' :      
                            result = student.remove_phone_number(removed_number)
                            print(f"{removed_number} has been removed successfully" if result else f"{removed_number} not found in list")
                        else:
                            print("\nDeletion cancelled")

                        try:
                            remove_another = int(input(f"\nRemove another phone number from list? [1-Yes, 0-No]: "))
                            if remove_another != 1:
                                break
                        except Exception:
                            print(f"\nError: Invalid Input, returning to menu")
                            break
            
            elif user_choice == 3:
                break

            else:
                print(f"\nError: Please enter a valid menu choice [1-3]")

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
    
    def edit_course_list(self, student:Student) -> int:
            while True:
                print("\n---Edit Course List---")
                print(f"1. Add Course\n"
                    "2. Remove Course\n"
                    "3. Go back\n")
                
                try:
                    user_choice = input("Enter your choice or -1 to go back: ").strip()
                    if user_choice == "":
                        raise ValueError("Input cannot be blank")
                    if not user_choice.lstrip("-").isdigit():
                        raise ValueError("Please enter a valid menu option [1-3]")
                    user_choice = int(user_choice)
                except ValueError as e:
                    print(f'\nError: {e}')
                    continue
                
                if user_choice == -1:
                    return -1
                
                elif user_choice == 1:
                    while True:
                        while True:
                            try:
                                course_num = input("Enter course name/number to add [e.g. CMPSC132]: ")
                                if len(course_num) > 0:
                                    break
                                else:
                                    raise ValueError(f"\nError: Please enter a valid course identifier [e.g. MATH360]")
                            except ValueError:
                                print(f"\nError: Please enter a valid course identifier [e.g. MATH360]")

                        while True:
                            try:
                                valid_sems = ['summer', 'fall', 'spring']
                                semester = input(f"Enter Semester of Completion for {course_num} [Fall/Spring/Summer]: ")
                                if semester.lower() in valid_sems:
                                    break
                                else:
                                    raise ValueError(f'\nError: Invalid Semester Value')
                            except ValueError:
                                print(f'\nError: Invalid Semester Value')
                        
                        while True:
                            try:
                                year = int(input(f"Enter Year of Completion for {semester}: "))
                                if 1900 <= year <= datetime.datetime.now().year:
                                    break
                                else:
                                    raise ValueError(f"\nError: Please enter a valid year for {semester}")
                            except ValueError:
                                print(f"\nError: Please enter a valid year for {semester}")

                        c_semester = Semester(semester,year)

                        while True:
                            try:
                                valid_inst_methods = ['classroom', 'hybrid', 'remote']
                                inst_method = input(f"Enter method of instruction [Classroom/Remote/Hybrid]: ")
                                if inst_method.lower() in valid_inst_methods:
                                    break
                                else:
                                    raise ValueError(f"\nError: Please enter a valid method of instruction for {course_num}")
                            except ValueError:
                                print(f"\nError: Please enter a valid method of instruction for {course_num}")
                        
                        while True:
                            try:
                                valid_status = ['completed', 'dropped', 'current']
                                status = input(f"Enter current status of course [Current/Completed/Dropped]: ")
                                if status.lower() in valid_status:
                                    break
                                else:
                                    raise ValueError(f"\nError: Please enter a valid status for {course_num}")
                            except ValueError:
                                print(f"\nError: Please enter a valid status for {course_num}")
                        
                        while True:
                            try:
                                valid_grades = ['a','b','c','d','f','n/a']
                                grade = input(f"Enter Course Grade [A-D,F, or n/a]: ")
                                if grade.lower() in valid_grades:
                                    break
                                else:
                                    raise ValueError(f"\nError: Please enter a valid grade for {course_num}")
                            except ValueError:
                                print(f"\nError: Please enter a valid grade for {course_num}")

                        new_Course = Course(course_num, c_semester, inst_method, status, grade)
                        student.append_course_list(new_Course)
                        print(f"\nThe following course has been added succesfully: \n{new_Course}")
                
                        try:    
                            add_another = int(input(f"\nAdd another course to list? [1-Yes, 0-No]: "))
                            if add_another != 1:
                                break
                        except Exception:
                            print(f"\nError: Invalid Input, returning to menu")
                            break
                
                elif user_choice == 2:
                    while True:
                        while True:
                            try:
                                removed_course_num = str(input(f"Enter Course Identifier to be removed (e.g. CMPSC132): ")).lower().strip()
                                if len(removed_course_num) > 0:
                                    break
                                else:
                                    raise ValueError(f"\nError: User input blank")
                            except ValueError:
                                print(f"\nError: User input blank")
                
                        confirm_remove = ''

                        while len(confirm_remove) <= 0 and confirm_remove != '-1' : 
                            confirm_remove = str(input(f"\nConfirm deletion of {removed_course_num} [1-Yes, 0-No]"))  

                            if len(confirm_remove) <= 0 :
                                print("Invalid input")
                            elif confirm_remove == '-1' : 
                                return -1
                            
                        if confirm_remove == '1' :      
                            result = student.remove_course_list(removed_course_num)
                            print(f"{removed_course_num} has been removed successfully" if result else f"{removed_course_num} not found in list")
                        else:
                            print("\nDeletion cancelled")

                        try:
                            remove_another = int(input(f"\nRemove another course from list? [1-Yes, 0-No]: "))
                            if remove_another != '1' :
                                break
                        except Exception:
                            print(f"\nError: Invalid input, returning to menu")
                            break

                elif user_choice == 3:
                    break

                else:
                    print(f"\nError: Please enter a valid menu option [1-3]")

    def construct_student(self) -> Student.Student : 
        print('\n---Add Student---')
        print("Enter -1 at any time to cancel\n")
        
        try : 
            print(f"Enter student's name : ")
            while True:
                try:
                    first_name:str = str(input("First : "))
                    if first_name == '-1' : 
                        return -1
                    
                    if not first_name.isalpha():
                         raise TypeError("Error: Please enter a valid first name.")
                    if len(first_name) > 0:
                        break
                    else:
                        raise ValueError("Error: Please enter a valid first name.")
                except ValueError:
                     print("Error: Please enter a valid first name.")
                except TypeError:
                     print("Error: Please enter a valid first name.")
            
            while True:
                try:
                    middle_name:str = str(input("Middle : "))

                    if middle_name == '-1' : 
                        return -1
                    if middle_name.isalpha() or len(middle_name) == 0:
                         break
                    else:
                         raise TypeError(f"Error: Please enter a valid middle name")
                #Note - Does not take middle names such as van de pol or Barrett-Saxon
                except TypeError:
                     print(f"Error: Please enter a valid middle name (if multiple, enter as one with each capitalized)")
            
            while True:
                try:
                    last_name:str = str(input("Last : "))
                    
                    if last_name == '-1' : 
                        return -1
                    if not last_name.isalpha():
                         raise TypeError("Error: Please enter a valid last name.")
                    if len(last_name) > 0:
                        break
                    else:
                        raise ValueError("Error: Please enter a valid last name.")
                except ValueError:
                     print("Error: Please enter a valid last name.")
                except TypeError:
                     print("Error: Please enter a valid last name.")

            name = str(Name(first_name, middle_name, last_name))
 
            print("Enter student's home address : ")
            new_street_adr:str = str(input("Street Address : "))
            while len(new_street_adr) <= 0 : 
                print("Invalid, address cannot be blank")
                new_street_adr = str(input("Street Address : "))

            new_city:str = str(input("City : "))
            while len(new_city) <= 0 :
                print("Invalid, City Name Cannot be blank")
                new_city = str(input("City : "))
            
            new_state:str = str(input("State : "))
            while len(new_state) <= 0 :
                print("Invalid, State cannot be blank")
                new_state:str = str(input("State : "))

            new_zipcode:str = str(input("Zipcode : "))
            while len(new_zipcode) <= 0 :
                print("Invalid, zipcode cannot be blank")
                new_zipcode:str = str(input("Zipcode : "))

            new_addr_type:str = str(input("Address Type : "))
            while len(new_addr_type) <= 0 : 
                print("Invalid, address type cannot be blank")
                new_addr_type:str = str(input("Address Type : "))

            new_Address = Address(new_street_adr, new_city, new_state, new_zipcode, new_addr_type)

            # (DONE)Revise for Int data type
            unique_id_number = False
            while not unique_id_number:
                try:
                    id_num:int = int(input("Enter student's id number: "))

                    if id_num == -1 : 
                        return -1
                    if id_num < 0:
                         raise ValueError("Error: Please enter a valid student ID number (must be positive number)")

                    if not self.__advisees.search(id_num) : 
                        unique_id_number = True 
                    else : 
                        print("ID Number already in use, try again")

                except ValueError:
                    print("Error: Please enter a valid student ID number (must be positive number)")
            
            print(f"Enter Student's Email Address : ")
            while True:
                try:
                    address:str = input("Email : ")
                    if len(address) > 0:
                        break
                    else:
                        raise ValueError(f"Error: Email Address Blank")
                except ValueError:
                    print(f"Error: Email Address Blank")

            while True:
                try:
                    add_type:str = input("Email Address Type (e.g. Work, Personal, Business etc.) : ")
                    if len(add_type) > 0:
                        break
                    else:
                        raise ValueError(f"Error: Email type blank")
                except ValueError:
                    print (f"Error: Email type blank")
            
            new_email = EmailAddress(address, add_type)

            print(f"Enter Student's Phone Number : ")
            while True:
                try:
                    new_number:str = input("Phone Number : ")
                    if len(new_number) > 0:
                        break
                    else:
                        raise ValueError("Error: Phone number blank")
                except ValueError:
                    print("Error: Phone number blank")

            while True:
                try:
                    new_number_type:str = input("Phone Type (e.g. Business, Personal, Cell) : ")
                    if len(new_number_type) > 0:
                        break
                    else:
                        raise ValueError("Error: Phone type blank")
                except ValueError:
                    print("Error: Phone type blank")
            
            new_phone_number:PhoneNumber = PhoneNumber(new_number, new_number_type)
            
            # Attempt to append phone number and return True or False for Success or Failure

            print("Enter student's birthdate: ")
            while True:
                try:
                    year:int = int(input("Year: "))
                   
                    if year == -1 : 
                        return -1
                    if year < 1000 or year > datetime.datetime.now().year:
                        raise ValueError(f"Error: Please enter a valid year")
                    else:
                        break
                except ValueError:
                     print(f"Error: Please enter a valid year")

            while True:
                try:
                    month:int = int(input("Month: "))
                    
                    if month == -1 : 
                        return -1
                    if month < 1 or month > 12:
                        raise ValueError(f"Error: Please enter a valid month")
                    else:
                        break
                except ValueError:
                    print(f'Error: Please enter a valid month for {year}')

            while True:
                try:
                    last_day_of_month = calendar.monthrange(year, month)[1]
                    month_to_str = calendar.month_name[month]
                    day:int = int(input("Day: "))

                    if day == -1 : 
                        return -1
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

                    if year2 == -1 : 
                        return -1
                    if year2 < 1900 or year2 > datetime.datetime.now().year:
                        raise ValueError(f"Error: Please enter a valid year")
                    else:
                        break
                except ValueError:
                     print(f"Error: Please enter a valid year")
            
            while True:
                try:
                    month2:int = int(input("Month: "))

                    if month2 == -1 : 
                        return -1
                    if month2 < 1 or month2 > 12:
                        raise ValueError(f"Error: Please enter a valid month")
                    else:
                        break
                except ValueError:
                    print(f'Error: Please enter a valid month for {year2}')

            while True:
                try:
                    day2:int = int(input("Day: "))

                    if day2 == -1 : 
                        return -1
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

                    if semester == '-1' : 
                        return -1
                    if semester.lower() in valid_sems:
                        break
                    else:
                        raise ValueError(f'Error: Please enter a valid start semester (summer/fall/spring)')
                except ValueError:
                    print(f'Error: Please enter a valid start semester (summer/fall/spring)')

            while True:
                try:
                    semester_year:int = int(input("Year: "))

                    if semester_year == -1 : 
                        return -1
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

                    if intended_major == '-1' : 
                        return -1
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
            new_student:Student.Student = Student.Student(name, new_Address, id_num, birthdate, acceptance_date, start_semester, intended_major)
            new_student.append_email_address(new_email)
            new_student.append_phone_number(new_phone_number)
            print(f'\n New Student ({new_student.get_name()}) Added Successfully!')
            return new_student
        except Exception as e : # No exceptions are setup atm, just returning None
            return None

    def delete_student(self) -> int : 
        while True:
            try:
                print('\n---Delete Student---')
                id_to_del = input("Enter id number of student you want to delete or -1 to go back : ")
                if id_to_del == "":
                    raise ValueError("User Input Blank")
                if not id_to_del.lstrip("-").isdigit():
                    raise ValueError("User Input Invalid")
                id_to_del = int(id_to_del)

                if id_to_del == -1 : # Go back a menu indicator
                    return 0
                break

            except ValueError as e:
                print(f"Error: {e}")
        
        student = self.__advisees.search(id_to_del)
        if student is not None : 
                student.display_data()

                while True:
                    try:
                        do_delete = input("\nIs this the correct student to delete? [1-Yes, 0-No] : ")
                        if do_delete == "":
                            raise ValueError("User Input Blank")
                        if do_delete not in ["0","1"]:
                            raise ValueError("User Input Invalid")
                        do_delete: bool = bool(int(do_delete))
                        break
                    except ValueError as e:
                        print(f"\nError: {e}")               

                if do_delete : 
                    #FIXME
                    # Call delete student(student) on advisor class here
                    self.__advisees.remove_data(student)
                    print("Student successfully deleted\n")
                    success = True
                    return 1
                else : 
                    print("\nWrong student indicated, searching for another student with same ID...")

        print("\nError: Failed to delete, student not found in your Advisee List")
        return -1

    def display_student(self) -> int : 
        print('\n---Display Student---')
        while True:
            try:
                id_to_display:int = int(input("Enter id number of student to display or -1 to go back : "))
                if id_to_display < -1:
                     raise ValueError("\nError: Please enter a valid student ID to display (must be positive number).\n")
                break
            except ValueError:
                print("\nError: Please enter a valid student ID to display (must be positive number).\n")

        # If user wishes to go back, return 0 to indicate this to main loop
        if id_to_display == -1 : 
            return 0 
        
        student = self.__advisees.search(id_to_display)
        if student is None : 
            print(f'\nError: Student ID Not Found in your Advisor Student List')
            return -1
        else : 
             print(student)
             return 1

    def display_advisees(self) -> None : 
        self.__advisees.display()

    def append_student(self, stud:Student.Student) -> None : 
         self.__advisees.append_node(stud)

    def get_advisees(self) -> linked_list : 
        return self.__advisees