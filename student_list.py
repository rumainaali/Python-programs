'''Date:20/04/2024
Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
'''

#Assign values to student list, cs marks, maths marks and eng marks
stu_list=['Shilpa','Rumaina','Rakhi','Keerthana','Sharon']
cs_marks=[80,98,95,85,75]
maths_marks=[90,99,56,86,80]
eng_marks=[45,80,75,95,98]

#initialize empty list to store students name
new_stu_list=[]

for i in range(len(stu_list)):
    if ((cs_marks[i]>=90 and maths_marks[i]>=90 and eng_marks[i]>=90) or 
        ((cs_marks[i]>=90 and maths_marks[i]>=80 and eng_marks[i]>=80) or  
        (maths_marks[i]>=90 and cs_marks[i]>=80 and eng_marks[i]>=80)  or 
        (eng_marks[i]>=90 and cs_marks[i]>=80 and maths_marks[i]>=80))):
     new_stu_list.append(stu_list[i])
print(new_stu_list)