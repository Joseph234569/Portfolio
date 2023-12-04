# Joseph
# 11/30/2023

# Takes two inputs from a user and either prints greater than,less than or equal to 10
def check_sum(num1, num2):
    total = num1 + num2
    if total > 10:
        print("The sum is greater than 10")
    elif total < 10:
        print("The sum is less than 10")
    else:
        print("The sum is equal to 10")