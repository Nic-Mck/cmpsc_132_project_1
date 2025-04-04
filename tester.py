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
          )
    

def edit_student_name(student:Student) -> bool :
    new_first:str = input("Enter new first name : ")
    new_middle:str = input("Enter new middle name : ")
    new_last:str = input("Enter new last name : ")
    student.set_name(Name(new_first, new_middle, new_last))
    return True

def edit_student_birthdate(student:Student) -> bool : 
    new_day:str = input("Enter new birthdate day : ")
    new_month:str = input("Enter new birthdate month : ")
    new_year:str = input("Enter new birthdate year : ")

    student.set_birthdate(Date(new_month, new_day, new_year))
    return True

def edit_acceptance_date(student:Student) -> bool : 
    new_day:str = input("Enter new acceptance day : ")
    new_month:str = input("Enter new acceptance month : ")
    new_year:str = input("Enter new acceptance year : ")

    student.set_acceptance_date(Date(new_month, new_day, new_year))
    return True

def edit_student_semester(student:Student) -> bool : 
    new:str = input("Enter new semester : ")
    year:int = int(input("Enter the year : "))

    student.set_semester(Semester(new, year))
    return True

def edit_student_intended_major(student:Student) -> bool :
    new:str = input("Enter new major : ")
    student.set_intended_major(new)
    return True

def add_email_address(student:Student) -> bool : 
    address:str = input("Enter new email address : ")
    add_type:str = input("Enter email address type : ")
    
    new_email = EmailAddress(address, add_type)

    # Attempt to append email and return True or False for Success or Failure
    return student.append_email_address(new_email)


def add_phone_number(student:Student) -> bool : 
    new_number:str = input("Enter new phone number : ")
    new_number_type:str = input("Enter phone number type (Business, Personal, Etc.) : ")
    
    new_phone_number:PhoneNumber = PhoneNumber(new_number, new_number_type)
    
    # Attempt to append phone number and return True or False for Success or Failure
    return student.append_phone_number(new_phone_number)




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
                case _ : # Default Case
                    raise Exception("Invalid submenu choice")
                
            break # Exit loop as student was found

    # If student wasn't found, raise exception
    if not success : 
        raise Exception("Student not found")

def construct_student() -> Student.Student : 
    try : 
        name:str = str(input("Enter student's name: "))
        id_num:int = int(input("Enter student's id number: "))
        birthdate:str = str(input("Enter students birthdate: "))
        acceptance_date:str = str(input("Enter student's acceptance date: "))
        semester:str = str(input("Enter current sememster: "))
        intended_major:str = str(input("Enter student's intended major: "))

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
                id_to_del:int = int(input("Enter id number of student you want to delete: "))
            
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
                id_to_display:int = int(input("Enter id number of student to display: "))

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