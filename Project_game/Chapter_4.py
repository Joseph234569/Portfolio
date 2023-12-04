import random
print("player runs towards a portal")
print("player sliding down a hole")
print("rocks falling down")
rocks = random.choice(["hit", "not hit"])
if rocks == "hit":
    print("failed level due to getting hit by rock")
    # restart chapter
elif rocks == "not hit":
    pass
print("4:left or 5:right")
key = input("enter your key:4,5")
if key == "4":
    print("the player will slide left")
elif key == "5":
    print("the player will slide right")


