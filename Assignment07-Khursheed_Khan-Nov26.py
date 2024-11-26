# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Khursheed Khan, Foundations of Programming - Python, Nov 24 2024
#   RRoot,1/1/2030,Created Script
#   First run, Nov 24 2024 ... second run Nov 26 2024 at 9:14am Pacific
# ------------------------------------------------------------------------------------------ #

"""
Course Registration Program

This script allows users to register students for courses, view current registrations,
save them to a JSON file, and load data on startup. The program uses exception handling
to manage file operations and input validation to ensure data integrity.

Features:
    - Register students for courses.
    - View all registered students and their courses.
    - Save and load data from a JSON file.

ChangeLog:
    Khursheed Khan, Nov 18 2024, First run
    RRoot, Jan 1 2030, Updated script structure
"""


import json
from json import JSONDecodeError


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
students: list[dict[str,str]] = [] # Set to empty
menu_choice: str = str() # Hold the choice made by the user.


class Person:

    __first_name: str
    __last_name: str

    def __init__(self, user_first_name:str, user_last_name:str):
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

    #def print_intro(self):
        #print(f'Hello, my name is {self.first_name} {self.last_name}')

    #@staticmethod
    #def print_intro_static():
        #print(self.first_name, self.last_name)
        #print("Hi I am the Student Class")

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}"

class Student(Person):
    __course_name: str
    def __init__(self, student_first_name:str, student_last_name:str,student_course_name:str): # Overloading __init__
        super().__init__(student_first_name, student_last_name) # Initializing parent class
        self.course_name = student_course_name # Initializing Student_Class Attrributes --> setting up consturctor, creating instance

    @property
    def course_name(self):
        return self.__course_name
    @course_name.setter
    def course_name(self, value):
        if value == '':
            raise ValueError("Course Name is required")
        self.__course_name = value


    def __str__(self):
        return f"{super().__str__()},course_name: {self.course_name}"

    @staticmethod
    def from_json(data):
        return Student(data['first_name'], data['last_name'], data['course_name']) #Need to understand what it is doing


class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    Methods:
        read_data_from_file(file_name, student_data):
            Reads student data from a specified JSON file and returns it as a list of dictionaries.
        write_data_to_file(file_name, student_data):
            Writes a list of student dictionaries to a specified JSON file.

    ChangeLog:
        Khursheed Khan, Nov 18 2024, first update
        RRoot, Jan 1 2030, Created Class
    """
    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list[dict[str,str]]):
    #def read_data_from_file(file_name:str, student_data:list[Student]):
        """
               Reads student data from a JSON file. If the file doesn't exist or contains invalid JSON, handles errors.

               Args:
                   file_name (str): Name of the file to read from.
                   student_data (list[dict[str, str]]): An initial list of student data.

               Returns:
                   list[dict[str, str]]: Updated list of student data read from the file.
               """

        try:
            file = open(file_name, "r")

            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
            for student in list_of_dictionary_data:  # Convert the list of dictionary rows into Student objects

                student_object: Student = Student(
                    student_first_name=student["FirstName"],
                    student_last_name=student["LastName"],
                    student_course_name=student["CourseName"]
                )
                #student_object: Student = Student(first_name=student["FirstName"],
                                                  #last_name=student["LastName"],
                                                  #course_name=student["CourseName"])
                ## I need to understand why the code snippet above did not work with first_name etc...
                
                student_data.append(student_object)

            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
            IO.output_error_messages("Creating the file") #Add this to create file if it does not exist
            file = open(file_name, "w")
            file.close()
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list[dict[str,str]]):
    #def write_data_to_file(file_name:str, student_data:list[Student]):
        """
        Writes student data to a JSON file.

        Args:
            file_name (str): Name of the file to write to.
            student_data (list[dict[str, str]]): List of student dictionaries to write.

        Returns:
            None
        """

        try:
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name, "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    Methods:
        output_error_messages(message, error):
            Displays a custom error message and optionally a technical error message.
        output_menu(menu):
            Displays a formatted menu to the user.
        input_menu_choice():
            Prompts the user to select a menu option and validates the choice.
        input_student_data(student_data):
            Collects student details from the user and adds them to the student data list.
        output_student_courses(student_data):
            Displays the list of registered students and their courses.

    ChangeLog:
        Khursheed Khan, Nov 18 2024, first update
        RRoot, Jan 1 2030, Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays a custom error message to the user.

        Args:
            message (str): A descriptive error message.
            error (Exception, optional): The technical error, if available.

        Returns:
            None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays a menu of choices to the user.

        Args:
            menu (str): The formatted menu string to display.

        Returns:
            None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        Prompts the user to select a menu option.

        Returns:
            str: The user's validated menu choice.
        """
        choice = "0" #Why needed?
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ["1", "2", "3", "4"]:  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message # clarify?
        return choice

    @staticmethod
    def input_student_data(student_data: list[dict[str,str]] = None) -> list[dict[str,str]]:
    #def input_student_data(student_data:list[Student]=None) -> list[Student]:
        """
        Collects student data (first name, last name, course) from the user.

        Args:
            student_data (list[dict[str, str]], optional): Existing student data to update.

        Returns:
            list[dict[str, str]]: Updated list of student data.
        """
        # Ensure student_data is a list
        if student_data is None:
            student_data = []

        try:
            # Collect student information
            first_name = input("What is the student's first name? ")
            last_name = input("What is the student's last name? ")
            course_name = input("What is the student's course? ")

            # Create a new Student object with the collected information
            student = Student(first_name, last_name, course_name)

            # Add the student to the list
            student_data.append(student)

        except ValueError as e:
            # This will catch the validation errors from first_name and last_name setters
            IO.output_error_messages("Invalid name entered!", e)
        except Exception as e:
            IO.output_error_messages("There was an error registering the student!", e)

        return student_data

    @staticmethod
    def output_student_courses(student_data: list[dict[str, str]]):
    #def output_student_courses(student_data:list[Student]):
        """
                Displays the list of registered students and their courses.

                Args:
                    student_data (list[dict[str, str]]): List of student dictionaries to display.

                Returns:
                    None
                """
        if student_data:
            print("Registered Students")
            for student in student_data:
                print(f"{student.first_name} {student.last_name} {student.course_name}")
        else:
            print("You have not registered yet")

#  End of function definitions

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)

    elif menu_choice == "2": # Display current data
        IO.output_student_courses(student_data=students)

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)

    elif menu_choice == "4":  # End the program
        print("Program ended, thanks")
        break  # out of the while loop
    else:
        print ("Please select a valid menu option 1, 2 or 3")

print ("Program Ended")