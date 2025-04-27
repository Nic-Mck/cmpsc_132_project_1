# Names: Nick McKenna, Edward Hu
# Class: CMPSC132
# Date of Final Revision: 4-27-2025

# This module is the User Interface for our Academic Advisor Student Management System

import Student
from StudentAttributes import *
import Advisor
import linked_list


# FIXME (Completed)
# DONE Add an Advisor
# DONE Delete an Advisor
# DONE Edit Advisor Info
# DONE Display Advisor Info 
# DONE Add students to advisee list+
# DONE Delete students from advisee list 

advisors:list[Advisor.advisor] = [
    Advisor.advisor("Bill Nye", "Science Guy", "Science Department"),
    Advisor.advisor("Mrs. Frizzle", "Advisory Advisor", "Advisory Department")
]

advisors[0].add_student(Student.Student("First Tester", "1234 Test Lane, Media PA", 0, "0/0/0000", "1/1/1111", "Fall", "Compsci"))
advisors[0].add_student(Student.Student("Second Tester", "5678 Campus DR, Media PA", 1, "1/1/1111", "2/2/2222", "Spring", "Engineering"))
advisors[0].add_student(Student.Student("Third Tester", "9101112 Road Road, Phil PA", 2, "2/2/2222", "3/3/3333", "Summer", "Finance"))

advisees = advisors[0].get_advisees()
advisees.head.get_data().set_course_list([Course('001', 'Fall', 'Classroom', 'Completed', 'A'),
                               Course('002', 'Spring', 'Hybrid', 'Dropped', 'N/A'),
                               Course('003', 'Winter', 'Remote', 'Current', 'A')])
advisees.head.get_next().get_data().set_course_list([Course('101', 'Summer', 'Classroom', "Current", 'C'),
                                                     Course('250', 'Fall', 'Remote', "Completed", 'B'),
                                                     Course('141', 'Winter', 'Hybrid', 'Dropped', 'N/A')])
advisees.head.get_next().get_next().get_data().set_course_list([Course('1201', 'Winter', 'Classroom', "Current", 'D'),
                                                                Course('50', 'Fall', 'Remote', "Completed", 'B'),
                                                                Course('14', 'Winter', 'Hybrid', 'Completed', 'F')])

def print_advisor_options() -> None : 
    print(
        f"\n---Admin/Main Menu---\n"
        "1. Choose Advisor [Login]\n"
        "2. Display Advisors\n"
        "3. Add Advisor\n"
        "4. Edit an Advisor\n"
        "5. Delete Advisor\n"
        "6. Exit\n"
        )
    
def print_advisor_sub_options() -> None : 
    print(
        f'1. Display Advisees\n'
        '2. Add Advisee\n'
        '3. Edit Advisee\n'
        '4. Back\n'
        )

def choose_advisor() -> None : 
    adv_to_choose:str = "" 

    while adv_to_choose != '-1' : 
        print('\n---Advisor Selection---')
        adv_to_choose:str = input("Please Enter Name of Advisor to Log In or -1 to go back : ").strip().lower()
        chosen_adv:Advisor.advisor = None
        found:int = 0 # 0 for not found, -1 if going back from next menu, 1 if found, -2 to go back from this menu

        if adv_to_choose == '-1' : break 

        for adv in advisors : 
            if adv.get_name().strip().lower() == adv_to_choose :
                chosen_adv = adv
                found = 1
                print("\nAdvisor Found!")
                break
        
        while found != 0 and found != -2:                         
            chosen_adv.print_main_menu() 
            response:str = str(input("Enter your choice: "))
            found = student_manipulation(adv, response)

        if found != -2 : 
            print("\nError: Advisor not found, please try again")

def delete_advisor() -> None : 

    # Admin password takes anything for scope of our assignment, but we put it in to show we were considering it

    admin_password = input(f"\nNotice: Admin access required [if you are administrator enter your password, or -1 to go back] : ")
    if admin_password == "-1" : return 

    adv_to_delete:str = ""

    while adv_to_delete != '-1' :
        print("\n---Delete Advisor(s)---\n")
        adv_to_delete = input("Enter the name of advisor to delete or -1 to go back : ").strip().lower()
        chosen_adv:Advisor.advisor = None 

        if adv_to_delete == "-1" : break

        for adv in advisors : 
            if adv.get_name().strip().lower() == adv_to_delete : 
                chosen_adv = adv 
                adv.display_advisor()

                while True:
                    try:
                        is_correct:bool = str(input(f'This advisor was found, is this correct? Confirm deletion [1-Yes, 0-No] : '))
                        if is_correct == "":
                            raise ValueError("User Input Blank")
                        if is_correct not in ["0","1"]:
                            raise ValueError("User Input Invalid")
                        break
                    except ValueError as e:
                        print(f"\nError: {e}")

                if is_correct == '1' : 
                    advisors.remove(chosen_adv)
                    print(f"\nAdvisor {adv_to_delete} has been successfully deleted!")
                    return 1
                else : 
                    print("Continuing search...")
                    continue
        
        print(f"\nError: Advisor ({adv_to_delete}) not found.")
    
def add_advisor() -> None : 

    user_input = None 
    while user_input != '-1' :
        print('\n---Add Advisor(s)---')
        print('Enter -1 at any time to go back')

        print("\nEnter the new advisors name : ")

        first_temp_name:str = ''
        while len(first_temp_name) <= 0 and first_temp_name != '-1' :
            first_temp_name = str(input("First Name : "))
            if len(first_temp_name) <= 0 : 
                print("\nError: Advisor First Name Blank")

        if first_temp_name == '-1' : break 

        middle_temp_name:str = ''
        middle_temp_name = str(input("Middle Name (if none, press enter to continue) : "))

        if middle_temp_name == '-1' : break 

        last_temp_name:str = ''
        while len(last_temp_name) <= 0 and last_temp_name != '-1' :
            last_temp_name = str(input("Last Name : "))
            if len(last_temp_name) <= 0 : 
                print("\nError: Advisor Last Name Blank")

        if last_temp_name == '-1' : break 

        temp_name = str(Name(first_temp_name, middle_temp_name, last_temp_name))

        valid_titles = ['admin', 'advisor', 'professor', 'associate professor', 'assistant professor', 'dr.',
                    'teaching assistant', 'learning assistant', 'doctor', 'researcher', 'lecturer', 'instructor',
                    'ta', 'la']

        temp_title:str = ''
        while True:#len(temp_title) <= 0 and temp_title != '-1' :
            temp_title = str(input("Enter the new advisors title [Advisor/Professor/Admin] : "))
            if temp_title == '-1' : break 
            if len(temp_title) <= 0 : 
                print("\nError: Advisor Title Blank")
            elif temp_title.strip().lower() not in valid_titles:
                print("\nError: Advisor Title Invalid")
            else:
                break

        temp_department:str = ''
        while len(temp_department) <= 0 and temp_department != '-1' :
            temp_department = str(input("Enter the new advisors department : "))
            if len(temp_department) <= 0 : 
                print("\nError: Advisor Department Blank")

        if temp_department == "-1" : break

        admin_password = input(f"\nNotice: Admin access required [if you are administrator enter your password, or -1 to go back] : ")
        if admin_password == "-1" : break

        advisors.append(Advisor.advisor(temp_name, temp_title, temp_department))
        print(f"\nAdvisor {temp_name} has been successfully added!")

def edit_advisor_search() -> None : 

    print('\n---Advisor Editing---')
    print('Enter -1 at any time to go back\n')

    name_to_search = ''
    adv_to_edit = None

    while len(name_to_search) <= 0 and name_to_search != '-1' :  

        name_to_search:str = str(input("Enter name of advisor to edit : ")).strip().lower()
        
        if len(name_to_search) <= 0 : 
            print("Error: Advisor not found in system\n")
            continue
    
    if name_to_search == '-1' : return

    admin_password = input(f"\nNotice: Admin access required [if you are administrator enter your password, or -1 to go back] : ")
    if admin_password == "-1" : return

    for adv in advisors : 
        if adv.get_name().strip().lower() == name_to_search : 
            adv.display_advisor()

            while True:
                try:
                    is_correct:str = str(input(f'Advisor {name_to_search} found, is this correct? [1-Yes, 0-No] : '))
                    if is_correct == '-1' : return 
                    if is_correct == "":
                        raise ValueError("User Input Blank\n")
                    if is_correct not in ["0","1"]:
                        raise ValueError("User Input Invalid\n")
                    break
                except ValueError as e:
                    print(f"\nError: {e}")

            if is_correct == '1' : 
                adv_to_edit = adv 
                break
            else : 
                print(f'Searching for another advisor by the name of {name_to_search}...')

    if adv_to_edit == None : 
        print("\nError: Advisor not found in system")
        edit_advisor_search()
        return
    
    edit_advisor(adv)

def edit_advisor(advisor_to_edit:Advisor.advisor) -> None : 
    def print_edit_advisor_submenu() -> None : 
        print('1. Edit Name\n'
              '2. Edit Title\n'
              '3. Edit Department\n')
    
    
    print(f'\n---{advisor_to_edit.get_name()} Edit Menu---')
    print('Enter -1 at any time to go back\n')
    print_edit_advisor_submenu()

    valid_choices:list[str] = ['1','2','3']
    choice:str = ''

    while choice not in valid_choices : 
        choice:str = str(input("Enter your choice: "))
        
        match choice : 
            case '1' : 
                first_temp_name:str = ''
                while len(first_temp_name) <= 0 and first_temp_name != '-1' :
                    first_temp_name = str(input("First Name : "))
                    if len(first_temp_name) <= 0 : 
                        print("\nError: Advisor First Name Blank")

                if first_temp_name == '-1' : break 

                middle_temp_name:str = ''
                middle_temp_name = str(input("Middle Name (if none, press enter to continue) : "))

                if middle_temp_name == '-1' : break 

                last_temp_name:str = ''
                while len(last_temp_name) <= 0 and last_temp_name != '-1' :
                    last_temp_name = str(input("Last Name : "))
                    if len(last_temp_name) <= 0 : 
                        print("\nError: Advisor Last Name Blank")

                if last_temp_name == '-1' : break 

                temp_name = str(Name(first_temp_name, middle_temp_name, last_temp_name))
                    
                if temp_name == '-1' : 
                    edit_advisor(advisor_to_edit)
                    return
                
                advisor_to_edit.set_name(temp_name)
                print('\nAdvisor name updated!\n')

            case '2' : 

                valid_titles = ['admin', 'advisor', 'professor', 'associate professor', 'assistant professor', 'dr.',
                    'teaching assistant', 'learning assistant', 'doctor', 'researcher', 'lecturer', 'instructor',
                    'ta', 'la']

                temp_title:str = ''
                while True:#len(temp_title) <= 0 and temp_title != '-1' :
                    temp_title = str(input("Enter the new advisors title [Advisor/Professor/Admin] : "))
                    if temp_title == '-1' : 
                        edit_advisor(advisor_to_edit)
                        return
                    if len(temp_title) <= 0 : 
                        print("\nError: Advisor Title Blank")
                    elif temp_title.strip().lower() not in valid_titles:
                        print("\nError: Advisor Title Invalid")
                    else:
                        break

                advisor_to_edit.set_title(temp_title)
                print('Advisor title updated\n')

            case '3' : 
                temp_department:str = ''

                while len(temp_department) <= 0 and temp_department != '-1' : 
                    temp_department = str(input("Enter the advisors new department: "))

                    if len(temp_department) <= 0 : 
                        print("\nError: Advisor Department Blank")

                if temp_department == '=1' : 
                    edit_advisor(advisor_to_edit)
                    return
                
                advisor_to_edit.set_department(temp_department)
                print('Advisor department updated\n')

            case '-1' : 
                edit_advisor_search()
                return
            case _ : 
                print("Error: Please select a valid menu option [1-3]")

    if choice == '-1' : return 

    edit_advisor(advisor_to_edit)
            
             
def student_manipulation(adv:Advisor.advisor, response:str) -> int : 
    found = 0
    match response : 
        case '1' : # Add student
            new_student = adv.construct_student()

            # If user indicated to go back a menu
            if new_student == -1 : 
                return -1
        
            adv.append_student(new_student)

            found = -1

        case '2' : # Edit Data
            success:int = 0

            # While user doesn't want to go back to the main menu
            while success != -1 :
                try :
                    success = adv.edit_student() 

                # Catch errors and report to user
                except Exception as e : 
                    print(f'\nFailed to edit student data due to error: {e}')
                    success = False

            found = -1

        case '3' : # Delete Student
            success:int = adv.delete_student()

            # While the user doesn't want to return to the main menu, Continue getting ID's to delete   
            while success != 0 : 
                success:int = adv.delete_student()

            found = -1

        case '4' : # Display Student
            success:int = adv.display_student()
            
            # While the user doesn't want to go back, keep getting ID's to display
            while success != 0 : 
                success:int = adv.display_student()

            found = -1
        
        case '5' : 
            adv.display_advisees()
            found = -1

        case '6' : # Exit
            adv_to_choose = None
            found = -2

        case _ : # Default Case
            print("Error: Please enter a valid menu choice [1-6]")
            found = -1

    return found


def main() -> None : 
    adv = Advisor.advisor("test Name", "Test Title", "Test Dept")
    exit_application:bool = False # Keeps track of wether or not app should close

    while not exit_application : 
        print_advisor_options()
        response:str = str(input("Enter your choice: "))

        match response : 
            case "1" : # Choose Advisor
                choose_advisor()
            case '2' : # Display Advisors : 
                admin_password = input(f"\nNotice: Admin access required [if you are administrator enter your password, or -1 to go back] : ")
                if admin_password == "-1" : continue
                print()
                print(f"Current Advisors in System:")
                print()
                for advisor in advisors : 
                    advisor.display_advisor()
            case '3' : # Add Advisor
                add_advisor()
            case '4' : # Edit Advisor 
                edit_advisor_search()
            case '5' : # Delete Advisor
                delete_advisor()
            case '6' : # Exit Application 
                exit_application = True
                print("\nExiting the Program.....\n")
                break

            case _ : # Default Case
                print(f"\nError: Please enter a valid menu choice [1-6]")

if __name__ == "__main__" : 
    main() 
    