import random
print("player will be surrounded with obstacles")
print("player running")
print("booby traps,barbed wire,flying bows/arrows")
obstacles = random.choice(["hit","not hit"])
print("Controls: Press 1 to Jump, Press 2 to Duck, Press 3 to Crawl")
key = input("Enter your key:1,2,3")
if key == "1":
    print("the player will jump")
elif key == "2":
    print("the player will duck")
elif key == "3":
    print("the player will crawl")
    if obstacles == "hit":
        print("Level failed due to being contacted with an obstacle")
        # restart chapter
    elif obstacles == "not hit":
        pass

