# Define the variables 'guess' and 'answer'
guess = 43 #You can replace this with any integer value
answer = 42 #You can replace this with any integer value

# Check if the guess is equal to the answer
if guess==answer:
    print("You got it for the first time")
else:
# Provide feedback based on guess
    print("Please guess higher")
else:
    print("Please guess lower")

# Get a new guess from the user
guess = int(input())

#Check if the new guess is correct
if guess == answer:
    print("Well done, you guessed it")
else:
    print("Sorry, you have not guesses correctly")