from student import find, register, update
screen = """
    WELCOME TO MY PAGE
Choose an option below to continue
-Enter R to register student.
-Enter F to find student.
-Enter U to update already existing student
-Enter Q to quit

"""
print(screen)

make_choice = input("Enter a value to continue: ").lower()

while make_choice != "q":
    if make_choice == "r":
        register

    elif make_choice == "f":
        find()

    elif make_choice == "u":
        update()

    make_choice = input("Enter a value to continue: ")