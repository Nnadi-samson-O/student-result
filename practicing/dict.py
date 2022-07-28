def register():
    name = input(("Enter your name here: "))
    age = int(input("Enter your age here: "))
    gender = input("Enter your gender here: ")
    student_info = (name, age, gender)
    subjects =[]
    number_of_subjects = 3

    for i in range(number_of_subjects):
        subject_name = input("Enter the name of subject: ")
        subjects.append(subject_name)

    subjects_score = {}
    for m in subjects:
        score = int(input(f"Enter your score for {m} here: "))
        subjects_score[m] = score
    print(student_info, subjects_score)
register()