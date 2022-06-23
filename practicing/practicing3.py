#calculate birth year
# Date_of_birth = input("Enter birth year: ")

# age = 2022 - int(Date_of_birth)

# print(age)

#whom_i_am = "mod commader parish and denary level"

# #This function checks if a value exist in a given expression
#print('mod' in whom_i_am)


weight = float(input("Enter your weight here: "))
unit = input("(k)g or (L)bs: ")
if unit.upper() == "k":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))

else:
    converted = weight * 0.45
    print("weight in kgs: "+ str(converted))