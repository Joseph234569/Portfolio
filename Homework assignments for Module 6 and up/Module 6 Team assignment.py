import random

n = random.randrange(1,100)
guess = int(input("Please guess number between 1 and 100"))
while 20!= guess:
    if guess < 20:
        print("Please guess lower")
        guess = int(input("Enter number again: "))
    elif guess > 20:
        print("Please guess higher")
    else:
        break
print("well done, you guessed it")
