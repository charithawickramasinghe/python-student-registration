import sys
from entities.student import Student


class UserMenu:
    __userinput = []

    def __init__(self):
        self.__student = Student()

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
        self.__userinput.append("Enter Note Title: ")
        self.__userinput.append("Enter Note Text: ")
        self.__userinput.append("Is completed(y/n): ")
        self.__userinput.append("Enter Note ID: ")

    # Print main menu.
    def main_menu(self):
        print("""
            1. Add New Note
            2. Select Note
            3. Update Note
            4. Delete Note
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

    def add_student(self):
        print('Add Student')

    def select_student(self):
        print('Select Student')

    def update_student(self):
        print('Update Student')

    def delete_student(self):
        print('Delete Student')

    def view_summary(self):
        print('View Summery')

    def quit(self):
        sys.exit(0)
