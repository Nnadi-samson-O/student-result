from student import Student

name = input("\nEnter name for new Student: ")
age = input("Enter age for new student: ")
gender = input("Enter student gender: ")

test_student = Student(name, age, gender)
print(f"\nHello! My name is {test_student.name} and I'm {test_student.age} years old, my gender is {test_student.gender}.")

test_student.enter_score()

print(f'\nSubjects for {test_student.name} are:\n{test_student.subjects}.')
scores_dict = test_student.subjects

header = f"""
=========================================
WELCOME TO STUDENT FINAL RESULT DISPLAY
---------------------------------------
student Name : {test_student.name}
student Age : {test_student.age}
student Gender : {test_student.gender}
=========================================
"""
print(header)
print("subjects:")
average_score = 0

for x in scores_dict.keys():
    y = scores_dict[x]
    print(f'{x}: {y[-1]}')
    average_score += y[-1]

new_average =average_score / len(scores_dict)
remarks = ""
if new_average <= 40:
    remarks = "poor"
elif new_average > 40:
    remarks = "average"
else:
    remarks = "good"

footer = f"""
===========================
Average: {new_average}
comment: {remarks}
===========================
"""
print(footer)

with open("student-result.txt", "w") as file:
    for student in header:
        file.writelines(header)
    file.write("\n")



