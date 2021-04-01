import sys


class UserMenu:
    __userinput = []

    def __init__(self):

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
