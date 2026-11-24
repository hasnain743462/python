# name="hassnain"
# age=18
# e_name = input("enter your name: ")
# e_age = input("enter your age :")
# if e_name == name and age >= e_age:
#     print("you are register in system")
# else :
#     print("you are not register in system")

name = input("enter your name :")
age = int(input("enter your age :"))
if age >= 18 :
    print(name, "you are eligible for vote casting")
else:
    print(name , "you are not eligible for vote casting dear", name, "if your age is under 18 you are not eligible")