def chapter_2():
    print("All of sudden you find yourself in a hedge maze")
scene = print("There are three paths to choose from")
print("Do you want to go left, right, or forward?")
print("To go right press 1, to go forward press 2, to go left press 3")
key = input("Enter your key: 1, 2, 3:")

if key == "1":
    print("Dead end, player will go back")
elif key == "2":
    print("Player will find a map")
elif key == "3":
    print("Player will find chests")