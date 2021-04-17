from datetime import datetime
from entities.student import Student


class Action:

    def __init__(self):
        self.__student = Student()

    # generate a unique number.
    def generate_index(self):
        return self.__file_ctrl.get_index()

    #  save the student details with a unique number.
    def add_note(self, student):
        student.id = self.generate_index()
        student.completed = self.check_boolean(student.completed)
        if str(student.completed) == 'True':
            student.completed_date = datetime.today().strftime('%Y-%m-%d')

        student.created_date = datetime.today().strftime('%Y-%m-%d')
        record = [str(student.id) + ",", str(student.title) + ",", str(student.text) + ",", str(student.created_date) + ",",
                  str(student.completed) + ",", str(student.completed_date) + "\n"]
        self.__file_ctrl.save_data(record)