import sys
from entities.student import Student
from handlers.action import Action


class UserMenu:

    def __init__(self):
        self.__userinput = []
        self.__student = Student()
        self.__action = Action()

        # user choice menu
        self.choices = {
            "1": self.add_student,
            "2": self.select_student,
            "3": self.update_student,
            "4": self.delete_student,
            "5": self.view_summary,
            "6": self.quit
        }

        # user input text
        self.__userinput.append("Enter Student Name: ")
        self.__userinput.append("Enter Student Address: ")
        self.__userinput.append("Enter Student Age: ")
        self.__userinput.append("Is completed(y/n): ")
        self.__userinput.append("Enter Student Id: ")

    # Print main menu.
    def main_menu(self):
        print("""
            1. Add New Student
            2. Select Student
            3. Update Student
            4. Delete Student
            5. View Summary
            6. Exit
        """)

    # Display user menu and ask response from user.
    def display_menu(self):

        while True:
            self.main_menu()

            choice = input("Enter the menu ID: ")

            action = self.choices.get(choice)

            if action:
                action()

            else:
                print("{0} is invalid".format(choice))

    # take student details from the user.
    def add_student(self):
        print('\n----- Add Student -----\n')
        self.__student.set_name(input(self.__userinput[0]))
        self.__student.set_address(input(self.__userinput[1]))
        self.__student.set_age(input(self.__userinput[2]))
        self.__student.set_completed(input(self.__userinput[3]))

        self.__action.add_note(self.__note)

    # display student data by Id.
    def select_student(self):
        print('\n----- Select Student -----\n')
        self.__student.id = input(self.__userinput[3])

        if int(self.__student.id) > 0:
            index = self.__action.check_availability(self.__student.id)
            if index > -1:
                self.__action.select_note(self.__student)
            else:
                print('Invalid Student Id.\n')
        else:
            print('Invalid Student id.\n')

    def update_student(self):
        print('Update Student')

    def delete_student(self):
        print('Delete Student')

    def view_summary(self):
        print('View Summery')

    def quit(self):
        sys.exit(0)
