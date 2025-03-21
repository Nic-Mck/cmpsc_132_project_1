import Student 

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
          )

def edit_student(students) -> None : 
    success:bool = False
    id_to_edit:int = int(input("Enter id number of student you wish to edit: "))
    
    for student in students : 
        if student.get_id_num() == id_to_edit : 
            print_edit_menu()
            sub_menu_choice:int = int(input("Enter submenu choice: "))

            match sub_menu_choice : 
                case 1 : # Name
                    new:str = input("Enter new name : ")
                    student.set_name(new)
                    success = True

                case 2 : # Birthdate
                    new:str = input("Enter new birthday : ")
                    student.set_birthdate(new)
                    success = True

                case 3 : #Acceptance Date
                    new:str = input("Enter new acceptance date : ")
                    student.set_acceptance_date(new)
                    success = True

                case 4 : # Semester 
                    new:str = input("Enter new semester : ")
                    student.set_semester(new)
                    success = True

                case 5 : # Intended Major
                    new:str = input("Enter new major : ")
                    student.set_intended_major(new)
                    success = True

                case _ : # Default Case
                    raise Exception("Invalid submenu choice")
                
            break # Exit loop as student was found

                # FIXME
                # We should probably also have options for editing email addresses and phone numbers,
                # But we would need to grab all of the necessary info to construct the objects from the user
                # And I am far too lazy to do that at this moment
                #
                # Ommitted option to change student id num as that is a unique identifier that should probably never change
                # Lots of these prolly SHOULDN'T ever change but it doesn't hurt to have the option


    if not success : 
        raise Exception("Student not found")

def construct_student() -> Student.Student : 
    name:str = str(input("Enter student's name: "))
    id_num:int = int(input("Enter student's id number: "))
    birthdate:str = str(input("Enter students birthdate: "))
    acceptance_date:str = str(input("Enter student's acceptance date: "))
    semester:str = str(input("Enter current sememster: "))
    intended_major:str = str(input("Enter student's intended major: "))

    try : 
        new_student:Student.Student = Student.Student(name, id_num, birthdate, acceptance_date, semester, intended_major)
        return new_student
    except Exception as e : # No exceptions are setup atm, just returning None
        return None

def main() -> None : 
    exit_application:bool = False # Keeps track of wether or not app should close
    students:list[Student.Student] = [Student.Student("Last, First", 1, "0/0/0000", "1/1/1111", "Fall", "Compsci")]

    while not exit_application : 
        print_main_menu() 
        response:int = int(input("Enter your choice: "))

        match response : 
            case 1 : # Add student
                new_student = construct_student()

                if new_student is None : 
                    print("Failed to create student, try again\n")
                else : 
                    students.append(new_student)

            case 2 : # Edit Data
                try :
                    edit_student(students) 

                # Catch errors and report to user
                except Exception as e : 
                    print(f'Failed to edit student data due to error: {e}')

            case 3 : # Delete Student
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

            case 4 : # Display Student
                success:bool = False
                id_to_display:int = int(input("Enter id number of student to display: "))

                for student in students : 
                    if student.get_id_num() == id_to_display : 
                        success = True
                        print(student)
                        break
                
                if not success : 
                    print("Failed to display student, student not found\n")

            case 5 : # Exit
                exit_application = True
                print("Exiting...")

            case _ : # Default Case
                print("Invalid input")



if __name__ == "__main__" : 
    main() 