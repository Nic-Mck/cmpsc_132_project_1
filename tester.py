import Student
from StudentAttributes import *
import Advisor
import linked_list


# FIXME
# Ad an Advisor
# Edit Advisor Info
# Display Advisor Info 
# Add students to advisee list+
# Delete students from advisee list 

def print_advisor_options() -> None : 
    print(
        f"\n---Main Menu---\n"
        "1. Choose Advisor\n"
        "2. Display Advisors\n"
        "3. Exit\n"
        )
    
def print_advisor_sub_options() -> None : 
    print(
        f'1. Display Advisees\n'
        '2. Add Advisee\n'
        '3. Edit Advisee\n'
        '4. Back\n'
        )
    

def main() -> None : 
    adv = Advisor.advisor("test Name", "Test Title", "Test Dept")
    exit_application:bool = False # Keeps track of wether or not app should close
    students:list[Student.Student] = [
                                      Student.Student("First Tester", "1234 Test Lane, Media PA", 0, "0/0/0000", "1/1/1111", "Fall", "Compsci"),
                                      Student.Student("Second Tester", "5678 Campus DR, Media PA", 1, "1/1/1111", "2/2/2222", "Spring", "Engineering"),
                                      Student.Student("Third Tester", "9101112 Road Road, Phil PA", 2, "2/2/2222", "3/3/3333", "Summer", "Finance")
                                    ]
    
    advisors:list[Advisor.advisor] = [
        Advisor.advisor("Mr. First Advisor", "Big Guy", "Big Guy Department"),
        Advisor.advisor("Mrs. Second Advisor", "Advisory Advisor", "Advisory Department")
    ]

    while not exit_application : 
        print_advisor_options()
        response:str = str(input("Enter your choice: "))

        match response : 
            case "1" : # Choose Advisor
                adv_to_choose:str = "" 

                while adv_to_choose != '-1' : 
                    print('\n---Advisor Selection---')
                    adv_to_choose:str = input("Enter name of advisor or -1 to go back : ")
                    chosen_adv:Advisor.advisor = None
                    found:int = 0 # 0 for not found, -1 if going back from next menu, 1 if found, -2 to go back from this menu

                    if adv_to_choose == '-1' : break 

                    for adv in advisors : 
                        if adv.get_name() == adv_to_choose :
                            chosen_adv = adv
                            found = 1
                            print("Advisor Found")
                            break
                    
                    while found != 0 and found != -2:                         
                        chosen_adv.print_main_menu() 
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

                                found = -1

                            case '3' : # Delete Student
                                success:int = adv.delete_student(students)

                                # While the user doesn't want to return to the main menu, Continue getting ID's to delete   
                                while success != 0 : 
                                    success:int = adv.delete_student(students)

                                found = -1

                            case '4' : # Display Student
                                success:int = adv.display_student(students)
                                
                                # While the user doesn't want to go back, keep getting ID's to display
                                while success != 0 : 
                                    success:int = adv.display_student(students)

                                found = -1

                            case '5' : # Exit
                                adv_to_choose = None
                                found = -2

                            case _ : # Default Case
                                print("Invalid input")

                    if found != -2 : 
                        print("\nAdvisor not found, try again")
                        adv_to_choose:str = input("Enter name of advisor or -1 to go back : ")
                        print()
            
            case '2' : # Display Advisors : 
                print()
                for advisor in advisors : 
                    advisor.display_advisor()

            case '3' : # Exit Application 
                exit_application = True
                break

if __name__ == "__main__" : 
    main() 
    