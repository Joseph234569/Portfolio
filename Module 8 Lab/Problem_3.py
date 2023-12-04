# Joseph
# 11/30/2023

# Takes a list that prints if the value 5 is in that list
def check_for_5(input_list):
    if 5 in input_list:
        print("5 is not present in the list")
    else:
        print("5 is not present in the list")

user_list = [int(x) for x in input("Enter a list of numbers seperated by spaces").split()]
check_for_5(user_list)