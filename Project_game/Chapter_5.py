import random

print("player reaches the bottom of the hole")
print("You are in a cave system with three paths")
print("Controls: To go Right press 1, to go Middle press 2, to go Left press 3")
key = input("Enter your key:1,2,3:")
chest = random.choice(["open", "dont open"])

if key == "1":
    print("The player will go right, into a dead end")
elif key == "2":
    print("The player will go middle, find a chest, and come to a dead end")
elif key == "3":
    input("Interact with chest: Yes or No")
    if chest == "open":
        print("RUN, Cave Monster has woken")
    elif chest == "dont open":
        print("No danger")
