from datetime import datetime
from entities.student import Student


class Action:

    def __init__(self):
        self.__student = Student()

    # generate unique number and save the student.
    def add_note(self, note):
        note.id = self.__file_ctrl.get_index()
        note.completed = self.check_boolean(note.completed)
        if str(note.completed) == 'True':
            note.completed_date = datetime.today().strftime('%Y-%m-%d')

        note.created_date = datetime.today().strftime('%Y-%m-%d')
        record = [str(note.id) + ",", str(note.title) + ",", str(note.text) + ",", str(note.created_date) + ",",
                  str(note.completed) + ",", str(note.completed_date) + "\n"]
        self.__file_ctrl.save_data(record)