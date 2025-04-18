import Student
from StudentAttributes import *
import advisor
import linked_list


# FIXME
# Ad an Advisor
# Edit Advisor Info
# Display Advisor Info 
# Add students to advisee list+
# Delete students from advisee list 

def main() -> None : 
    adv = advisor.advisor("test Name", "Test Title", "Test Dept")
    exit_application:bool = False # Keeps track of wether or not app should close
    students:list[Student.Student] = [
                                      Student.Student("First Tester", "1234 Test Lane, Media PA", 0, "0/0/0000", "1/1/1111", "Fall", "Compsci"),
                                      Student.Student("Second Tester", "5678 Campus DR, Media PA", 1, "1/1/1111", "2/2/2222", "Spring", "Engineering"),
                                      Student.Student("Third Tester", "9101112 Road Road, Phil PA", 2, "2/2/2222", "3/3/3333", "Summer", "Finance")
                                    ]

    while not exit_application : 
        adv.print_main_menu() 

        response:str = str(input("Enter your choice: "))

        match response : 
            case '1' : # Add student
                new_student = adv.construct_student(students)

                if new_student is None : 
                    print("Failed to create student, try again\n")
                else : 
                    students.append(new_student)

            case '2' : # Edit Data
                success:int = 0

                # While user doesn't want to go back to the main menu
                while success != -1 :
                    try :
                        success = adv.edit_student(students) 

                    # Catch errors and report to user
                    except Exception as e : 
                        print(f'Failed to edit student data due to error: {e}')
                        success = False

            case '3' : # Delete Student
                success:int = adv.delete_student(students)

                # While the user doesn't want to return to the main menu, Continue getting ID's to delete   
                while success != 0 : 
                    success:int = adv.delete_student(students)

            case '4' : # Display Student
                success:int = adv.display_student(students)
                
                # While the user doesn't want to go back, keep getting ID's to display
                while success != 0 : 
                     success:int = adv.display_student(students)

            case '5' : # Exit
                exit_application = True
                print("Exiting...")

            case _ : # Default Case
                print("Invalid input")



if __name__ == "__main__" : 
    main() 
    