import Student
from StudentAttributes import *

def print_main_menu() -> None : 
    print(f'\n1. Add Student\n'
          '2. Edit Student Data\n'
          '3. Delete Student\n'
          '4. Display Student Data\n'
          '5. Exit\n'
         )
    
def print_edit_menu() -> None : 
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
    

def edit_student_name(student:Student) -> bool :
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

    student.set_name(Name(new_first, new_middle, new_last))
    return True

def edit_student_birthdate(student:Student) -> bool : 

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

    student.set_birthdate(Date(new_month, new_day, new_year))
    return True

def edit_acceptance_date(student:Student) -> bool : 
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

    student.set_acceptance_date(Date(new_month, new_day, new_year))
    return True

def edit_student_semester(student:Student) -> bool : 
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

    student.set_semester(Semester(new, year))
    return True

def edit_student_intended_major(student:Student) -> bool :
    while True:
            new:str = input("Enter new major : ")
            if len(new) > 0:
                break
            else:
                print("Error: Intended major cannot be blank")

    student.set_intended_major(new)
    return True

def add_email_address(student:Student) -> bool : 
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

def add_phone_number(student:Student) -> bool : 
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

def edit_home_address(student:Student) -> bool : 
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



def edit_student(students) -> None : 
    success:bool = False
    id_to_edit:int = int(input("Enter id number of student you wish to edit: "))
    
    for student in students : 
        if student.get_id_num() == id_to_edit : 
            print_edit_menu()
            sub_menu_choice:int = int(input("Enter submenu choice: "))

            match sub_menu_choice : 
                case 1 : # Name
                    success = edit_student_name(student)
                case 2 : # Birthdate
                    success = edit_student_birthdate(student)
                case 3 : #Acceptance Date
                    success = edit_acceptance_date(student)
                case 4 : # Semester 
                    success = edit_student_semester(student)
                case 5 : # Intended Major
                    success = edit_student_intended_major(student)
                case 6 : # Add an email address
                    success = add_email_address(student)
                case 7 : # Add a phone number
                    success = add_phone_number(student)
                case 8 : # Edit Address
                    success = edit_home_address(student)
                case _ : # Default Case
                    raise Exception("Invalid submenu choice")
                
            break # Exit loop as student was found

    # If student wasn't found, raise exception
    if not success : 
        raise Exception("Student not found")

def construct_student() -> Student.Student : 
    try : 
        while True:
            name:str = str(input("Enter student's name: "))
            if len(name) > 0:
                break
            else:
                print("Invalid input. Please enter a valid student Name.")

        # Revise for Int data type
        while True:
            try:
                id_num:int = int(input("Enter student's id number: "))
                if id_num < 0 :
                    print("Invalid input. Student ID number cannot be negative")
                else:
                    break
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
        new_student:Student.Student = Student.Student(name, '', id_num, birthdate, acceptance_date, semester, intended_major)
        return new_student
    except Exception as e : # No exceptions are setup atm, just returning None
        return None

def main() -> None : 
    exit_application:bool = False # Keeps track of wether or not app should close
    students:list[Student.Student] = [Student.Student("Last, First", "", 1, "0/0/0000", "1/1/1111", "Fall", "Compsci")]

    while not exit_application : 
        print_main_menu() 

        response:str = str(input("Enter your choice: "))

        match response : 
            case '1' : # Add student
                new_student = construct_student()

                if new_student is None : 
                    print("Failed to create student, try again\n")
                else : 
                    students.append(new_student)

            case '2' : # Edit Data
                try :
                    edit_student(students) 

                # Catch errors and report to user
                except Exception as e : 
                    print(f'Failed to edit student data due to error: {e}')

            case '3' : # Delete Student
                success:bool = False
                while True:
                    try:
                        id_to_del:int = int(input("Enter id number of student you want to delete: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid student ID to delete.")
            
                # Find student with matching ID and delete from students array
                for student in students : 
                    if student.get_id_num() == id_to_del : 
                        students.remove(student)
                        print("Student successfully deleted\n")
                        success = True
                        break
                
                if not success : 
                    print("Failed to delete, student not found\n")

            case '4' : # Display Student
                success:bool = False
                while True:
                    try:

                        id_to_display:int = int(input("Enter id number of student to display: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid student ID to display.")

                for student in students : 
                    if student.get_id_num() == id_to_display : 
                        success = True
                        print(student)
                        break
                
                if not success : 
                    print("Failed to display student, student not found\n")

            case '5' : # Exit
                exit_application = True
                print("Exiting...")

            case _ : # Default Case
                print("Invalid input")



if __name__ == "__main__" : 
    main() 