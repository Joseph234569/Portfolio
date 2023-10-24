




if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else: # guess must be greater than answer
        print("Please guess lower")
    guess = int(input)