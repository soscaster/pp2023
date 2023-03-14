# -*- coding: utf-8 -*-

import curses
import math
import numpy as np
import os
# This code is for Windows : os.system("cls")
clear = lambda: os.system('clear')

screen = curses.initscr()

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob


class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit


class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark


class Manage:

    # The constructor, we're using dictionary to store the data
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.screen = curses.initscr()

    # The student input function definition
    def input_students(self):
        self.screen.clear()
        self.screen.addstr("----- WELCOME -----")
        self.screen.refresh()
        # print("----- WELCOME -----")

        # Input the number of students are going to be input with curses
        self.screen.addstr("Number of students you want to import: ")
        self.screen.refresh()
        stunum = int(self.screen.getstr())
        # stunum = int(input("Number of students you want to import: "))

        # Set i = 0, then i = i+1 to create a loop to input the student information
        i = 0

        # Input the student information by using for loop and append the information to the dictionary
        for _ in range(stunum):
            i = i + 1
            self.screen.addstr("Let's input information for Student No. " + str(i))
            # print("Let's input information for Student No.", i)
            self.screen.refresh()

            # print("---------------------------")
            self.screen.addstr("Student ID: ")
            self.screen.refresh()
            stu_id = str(self.screen.getstr())
            # stu_id = str(input("Student ID: "))
            self.screen.addstr("Student name: ")
            self.screen.refresh()
            stu_name = str(self.screen.getstr())
            # stu_name = str(input("Student name: "))
            self.screen.addstr("Student DOB: ")
            self.screen.refresh()
            stu_dob = str(self.screen.getstr())
            # stu_dob = str(input("Student DOB: "))
            
            # Create a new student object
            student = Student(stu_id, stu_name, stu_dob)
            # Add the student object to the dictionary
            self.students[stu_id] = student

            # One more way to add the student information to the dictionary
            # students[stu_id] = {"id": stu_id, "name": stu_name, "dob": stu_dob}

            self.screen.addstr("Student No. " + str(i) + " information has been imported successfully!")

            # print("Student No.", i, " information has been imported successfully!")
            # print("--------------------------------------------")

    def input_courses(self):
        # Input the number of courses are going to be input using curses

        self.screen.addstr("Number of courses you want to import: ")
        self.screen.refresh()
        cou_num = int(self.screen.getstr())
        # cou_num = int(input("Number of courses you want to import: "))

        # Set i = 0, then i = i+1 to create a loop to input the course information
        i = 0

        # Input the course information by using for loop and append the information to the dictionary
        for i in range(cou_num):
            i = i + 1
            self.screen.addstr("Let's input information for Course No. " + str(i))
            # print("Let's input information for Course No.", i)
            self.screen.addstr("Course ID: ")
            self.screen.refresh()
            cou_id = str(self.screen.getstr())
            # cou_id = str(input("Course ID: "))
            self.screen.addstr("Course name: ")
            self.screen.refresh()
            cou_name = str(self.screen.getstr())
            # cou_name = str(input("Course name: "))
            self.screen.addstr("Course credit(s): ")
            self.screen.refresh()
            cou_credit = int(self.screen.getstr())
            # cou_credit = int(input("Course credit(s): "))

            # Create a new course object
            course = Course(cou_id, cou_name, cou_credit)
            # Add the course object to the dictionary
            self.courses[cou_id] = course

            self.screen.addstr("Course No. " + str(i) + " information has been imported successfully!")
            # print("Course No.", i, " information has been imported successfully!")
            # print("--------------------------------------------")

    # List all the courses and students' information - ID, name, (DOB) using curses
    def list_all(self):
        # Print the list of courses
        self.screen.addstr("Input completed! ")
        self.screen.addstr("List of courses: ")
        # print("Input completed!")
        # print("List of courses: ")
        
        # Scan the dictionary and print the information
        for cou_id in self.courses:
            self.screen.addstr("ID: " + str(self.courses[cou_id].id) + ", Course Name: " + str(self.courses[cou_id].name) + ", Course Credit(s): " + str(self.courses[cou_id].credit))
            # print(f"ID: {self.courses[cou_id].id}, Course Name: {self.courses[cou_id].name}, Course Credit(s): {self.courses[cou_id].credit}")
        
        # print("----------------------------")
        self.screen.addstr("List of students: ")
        # print("List of students: ")

        # Scan the dictionary and print the information
        for stu_id in self.students:
            self.screen.addstr("ID: " + str(self.students[stu_id].id) + ", Name: " + str(self.students[stu_id].name) + ", DOB: " + str(self.students[stu_id].dob))
            # print(f"ID: {self.students[stu_id].id}, Name: {self.students[stu_id].name}, DOB: {self.students[stu_id].dob}")
        # print("--------------------------------------------")

    # Input the mark for each student in each course (choose the course first, then choose the student) using curses
    def input_marks(self):
        # Input the course ID using curses
        self.screen.addstr("Please input the course ID you want to input mark: ")
        self.screen.refresh()
        cou_id = str(self.screen.getstr())
        # cou_id = str(input("Please input the course ID you want to input mark: "))
        
        # Check if the course ID is in the dictionary
        if cou_id in self.courses:
            self.screen.addstr("Course found!")
            # print("Course found!")
            self.screen.addstr("Course ID: " + str(self.courses[cou_id].id) + ", Course name: " + str(self.courses[cou_id].name))
            # print("Course name: ", self.courses[cou_id].name)
            # print("----------------------------")

            # stu_id = str(input("Please input the student ID you want to input mark: "))

            # Input marks for each student in the course
            for stu_id in self.students:
                # print("Student found!")
                self.screen.addstr("Student ID: " + str(self.students[stu_id].id) + ", Student name: " + str(self.students[stu_id].name))
                # print("Student ID: ", self.students[stu_id].id)
                # print("Student name: ", self.students[stu_id].name)
                self.screen.addstr("Please input the mark: ")
                self.screen.refresh()
                mark = float(self.screen.getstr())
                # mark = float(input("Please input the mark: "))
                if mark >= 0 and mark <= 20:
                    key = (stu_id, cou_id)
                    mark = math.floor(mark)
                    # Create a new mark object
                    markre = Mark(stu_id, cou_id, mark)
                    # Add the mark object to the dictionary
                    self.marks[stu_id] = markre

                    # One more way to add the mark information to the dictionary
                    # self.marks[stu_id] = {"id": stu_id, "course": cou_id, "mark": mark}

                    self.screen.addstr("Mark information has been imported successfully!")
                    # print("Mark information has been imported successfully!")
                    # print("--------------------------------------------")
                else:
                    self.screen.addstr("Invalid mark!")
                    # print("Invalid mark!")
                    self.screen.addstr("Please input the mark again!")
                    # print("Please input the mark again!")
                    # print("--------------------------------------------")
                    
                    # Show the mark input menu again
                    self.input_marks()

            else:
                self.screen.addstr("Student not found!")
                # print("Student not found!")
        else:
            self.screen.addstr("Course not found!")
            # print("Course not found!")

    def show_marks(self):
        clear()
        self.screen.addstr("Please input the course ID you want to show mark: ")
        self.screen.refresh()
        cou_id = str(self.screen.getstr())
        # cou_id = str(input("Please input the course ID you want to show mark: "))
        if cou_id in self.courses:
            # print("--------------------------------------------")
            self.screen.addstr("Course found!")
            # print("Course found!")
            self.screen.addstr("Course ID: " + str(self.courses[cou_id].id) + ", Course name: " + str(self.courses[cou_id].name))
            # print("Course name: ", self.courses[cou_id].name)
            # print("----------------------------")
            self.screen.addstr("List of marks: ")
            # print("List of marks: ")

        # Iterate over the marks dictionary and display the marks for the specified course
            for stu_id in self.marks:
                mark = self.marks[stu_id]
                if mark.course == cou_id:
                    self.screen.addstr("Student ID: " + str(mark.student) + ", Mark (rounded): " + str(mark.mark))
                    # print(f"Student ID: {mark.student}, Mark (rounded): {mark.mark}")
            # print("----------------------------")
            self.continue_or_not()
        else:
            self.screen.addstr("Course not found!")
            # print("Course not found!")

    # Calculate the GPA for each student (choose the student first)
    # using math and numpy modules
    def gpa_calculator(self):
        clear()
        self.screen.addstr("Please input the student ID you want to calculate GPA: ")
        self.screen.refresh()
        stu_id = str(self.screen.getstr())
        # stu_id = str(input("Please input the student ID you want to calculate GPA: "))
        if stu_id in self.students:
            self.screen.addstr("Student found!")
            # print("Student found!")
            self.screen.addstr("Student ID: " + str(self.students[stu_id].id) + ", Student name: " + str(self.students[stu_id].name))
            # print("Student name: ", self.students[stu_id].name)
            # print("----------------------------")

            # Calculate the GPA using numpy
            marks = []

            # Get the marks for the specified student
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    marks.append(mark.mark)

            # Get course credits for the specified student
            credits = []
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    credits.append(self.courses[mark.course].credit)

            # Calculate the GPA
            # GPA = (sum of marks*credit)/sum of credit
            gpa = np.average(marks, weights=credits)
            self.screen.addstr("GPA: " + str(gpa))
            # print(f"GPA: {gpa}")
            # print("--------------------------------------------")
            self.continue_or_not_sort()
        else:
            self.screen.addstr("Student not found!")
            # print("Student not found!")

    # Sort student list by GPA descending order
    def sort_by_gpa(self):
        clear()
        self.screen.addstr("Sort by GPA descending order")
        # print("Sort by GPA descending order")
        # print("----------------------------")

        # Create a new dictionary to store the GPA
        gpa = {}

        # Calculate the GPA for each student
        for stu_id in self.students:
            marks = []
            credits = []
            for key in self.marks:
                mark = self.marks[key]
                if mark.student == stu_id:
                    marks.append(mark.mark)
                    credits.append(self.courses[mark.course].credit)
            gpa[stu_id] = np.average(marks, weights=credits)

        # Sort the GPA dictionary by GPA descending order
        gpa = dict(sorted(gpa.items(), key=lambda item: item[1], reverse=True))

        # Print the sorted GPA dictionary
        for stu_id in gpa:
            self.screen.addstr("Student ID: " + str(stu_id) + ", GPA: " + str(gpa[stu_id]))
            # print(f"Student ID: {stu_id}, GPA: {gpa[stu_id]}")
        # print("--------------------------------------------")
        exit()

    # Create a function to ask if the user wants to continue or run GPA count function
    def continue_or_not(self):
        while True:
            # Ask the user if they want to continue or not
            self.screen.addstr("Do you want to continue? (Y/N): ")
            self.screen.refresh()
            continue_or_not = str(self.screen.getstr())
            # continue_or_not = str(input("Do you want to continue? (Y/N): "))
            
            # If the user inputs Y, then the program will continue
            if continue_or_not == "Y":
                self.show_marks()
            
            # If the user inputs N, then the program will stop
            elif continue_or_not == "N":
                self.gpa_calculator()
            
            # If the user inputs other characters, then the program will ask the user to input again
            else:
                self.screen.addstr("Please input Y or N!")
                # print("Please input Y or N!")

    # Create a function to ask if the user wants to continue or run sort GPA function
    def continue_or_not_sort(self):
        while True:
            # Ask the user if they want to continue or not
            self.screen.addstr("Do you want to continue? (Y/N): ")
            self.screen.refresh()
            continue_or_not = str(self.screen.getstr())
            # continue_or_not = str(input("Do you want to continue? (Y/N): "))
            
            # If the user inputs Y, then the program will continue
            if continue_or_not == "Y":
                self.gpa_calculator()
            
            # If the user inputs N, then the program will stop
            elif continue_or_not == "N":
                self.sort_by_gpa()
            
            # If the user inputs other characters, then the program will ask the user to input again
            else:
                self.screen.addstr("Please input Y or N!")
                # print("Please input Y or N!")

manage = Manage()
clear()
manage.input_students()

# Wait for 3 seconds
print("Please wait for 3 seconds...")
import time
time.sleep(3)
# os.system("cls")
clear()

# Continue
manage.input_courses()

# Wait for 3 seconds
print("Please wait for 3 seconds...")
time.sleep(3)
# os.system("cls")
clear()

# Continue
manage.list_all()
manage.input_marks()
while True:
    # print("-----------------")
    # print("Input mark for the course completed!")
    screen.addstr("-----------------")
    screen.addstr("Input mark for the course completed!")
    # print("Do you want to continue with other course? (Y/N)")
    screen.addstr("Do you want to continue with other course? (Y/N)")
    screen.addstr("Your choice: ")
    screen.refresh()
    choice = str(screen.getstr())
    # choice = input("Your choice: ")
    if choice == "Y":
        manage.input_marks()
    elif choice == "N":
        manage.show_marks()
    else:
        screen.addstr("Invalid choice. Please try again!")
        # print("Invalid choice. Please try again!")
        continue
    