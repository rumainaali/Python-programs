''' Date:20/04/2024
Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.
'''

# Assign student names and their marks in CS
student_names = ["Sam", "Amina", "Zara", "Sameera", "Abdul"]
cs_marks = [90, 55, 80, 40, 45]
pass_mark = 50

# initialize empty list to store passed students and failed students
passed_students = []
failed_students_count = 0

# iterate through the marks, check for the  pass or fail
for i in range(len(student_names)):
    if cs_marks[i] >= pass_mark:
        passed_students.append(f"{student_names[i]}:{cs_marks[i]}")
    else:
        failed_students_count += 1

# print passed students
print("Students passed:")
for student in passed_students:
    print(student)

# print number of failed students
print("Number of failed students:", failed_students_count)
