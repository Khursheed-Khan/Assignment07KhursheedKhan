class Student:

    first_name: str
    last_name: str

    def __init__(self, user_first_name, user_last_name):
        self.first_name = user_first_name
        self.last_name = user_last_name


class IO:
    @staticmethod
    def input_data_to_table(student_data: list[Student]):
        try:
            student_first_name = input("First name: ")
            if not student_first_name.isalpha():
                raise ValueError ("First name must be alphanumeric")
            student_last_name = input("Last name: ")
            if not student_last_name.isalpha():
                raise ValueError ("Last name must be alphanumeric")

            call = Student(student_first_name, student_last_name)
            student_data.append(call)

        except ValueError as e:
            print("Only use names without numbers ",e)

        return student_data

roster = []
while True:
    roster = IO.input_data_to_table(roster)
    for student in roster:
        print(student.first_name, student.last_name)
    if input("Add another? (y/n) ").lower() [0]== "n":
        break



