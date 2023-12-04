# Joseph
# 12/01/2023

# A while loop that asks the user to enter a number, continues to ask for a number until the sum of the list is greater than 100
numbers = []
sum = 0
while sum <= 100:
    num = float(input("Please enter a number: "))
    numbers.append(num)
    sum += num
print("Sum of entered numbers is greater than 100. The numbers entered were: ", numbers)