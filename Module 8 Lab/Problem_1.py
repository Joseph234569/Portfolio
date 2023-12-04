# Joseph
# 11/30/2023

# Takes two user inputs from a user and prints if their equal or not
def check_equality(num1, num2):
    if num1 == num2:
        print("numbers are equal")
    else:
        print("numbers are not equal")

# Taking inputs from user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
check_equality(number1, number2)


