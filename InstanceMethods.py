class Student:

    __first_name: str
    __last_name: str

    def __init__(self, user_first_name, user_last_name):
        self.first_name = user_first_name
        self.last_name = user_last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value):
        if (not value.isalpha()):
            raise ValueError("First Name must be alphanumeric")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value):
        if (not value.isalpha()):
            raise ValueError("Last Name must be alphanumeric")
        self.__last_name = value

    def print_intro(self):
        print(f'Hello, my name is {self.first_name} {self.last_name}')

    @staticmethod
    def print_intro_static():
        #print(self.first_name, self.last_name)
        print("Hi I am the Student Class")

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}"

    @first_name.setter
    def first_name(self, value):
        if (not value.isalpha()):
            raise ValueError("First Name must be alphanumeric")
        self.__first_name = value

    @last_name.setter
    def last_name(self, value):
        if (not value.isalpha()):
            raise ValueError("Last Name must be alphanumeric")
        self.__last_name = value

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

Student.print_intro_static()

roster = []
while True:
    roster = IO.input_data_to_table(roster)
    for student in roster:
        print(student)
        str(student)
        student.print_intro() # Why do I need an argument here... because I was using upper case S... goofyball.
        #print(student.first_name, student.last_name)
    if input("Add another? (y/n) ").lower() [0]== "n":
        break

