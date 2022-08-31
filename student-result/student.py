# """
# this creates students object.
# """
# class Student:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.subjects = {}

#     def enter_score(self):
#         number_of_subjects = int(input(f"How many subjects do you want to offer {self.name} : "))

#         for i in range(number_of_subjects):
#             subject_name = input(f"\nEnter name of subject - {i+1}: ")
#             number_of_scores = 5
#             score_list = []

#             for z in range(number_of_scores):
#                 score = int(input(f"Enter score {z+1} for {subject_name}: "))
#                 score_list.append(score)

#             total = sum(score_list)
#             score_list.append(total)


#             self.subjects[subject_name] = score_list
            
    
def student_input():
    instruction = """
    CREATE A DICTIONARY THAT IS GOING TO ACCEPT THE FOLLOWING INPUT FROM THE USER:
    (1). The student user name
    (2). Number of subject that he is going to offer and the name of the subjects
    (3). The score of each subjects

    """
    print(instruction)
    # thisdict = {"onyebuchi":{"maths":40, "english":50} }
    # print(thisdict)
    thisdict = {}
    dict_of_subjet_score = {}


    number_of_student = int(input("Enter the number of students you want to print: "))
    for x in range(number_of_student):
        name = input("Enter the name of student: ")
        number_of_subject = 2


        for i in range(number_of_subject):
            subject_name = input(f"Enter the name of the subject that you want to offer {name}: ")


            for s  in subject_name[i]:
                score = int(input(f"Enter score for {subject_name}: "))
                dict_of_subjet_score[subject_name] = score
            print(dict_of_subjet_score)

        thisdict[name] = dict_of_subjet_score
    print(thisdict)
student_input()