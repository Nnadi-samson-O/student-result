students = []

number_of_students = int(input("how many students are in this class: "))

for student in range(number_of_students):
    name = input("Enter name: ")
    subjects = int(input("enter how many subjects you want to offer: "))
    for subject in range(subjects):
        name_of_subject = input("Enter name of subject: ")
        students.append([name,name_of_subject])

print(students)