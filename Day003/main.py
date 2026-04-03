print("Welcome to Treasure Island Game.")
print("You're on an uncharted island to find the treasure.")
print("")
print("_____________________🚶🏽‍♂️‍➡️️_____________________")
choice1 = input("A path splits ahead, choose Left or Right (l/r): ").lower()

if choice1 == "r":
    print("")
    print("🚶🏽‍♂️‍➡️﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏🏛️﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
    print("You reach a lake. A ruined temple stands in the middle.")
    choice2 = input('Type "b" to find a boat. Type "s" to swim across: ').lower()

    if choice2 == "b":
        print("")
        print("️﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏🚣🏾🏛️﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")
        print("You found an old boat and reached the temple.")
        choice3 = input("You found 3 doors Fish, Moon, Snake, choose one(f/m/s): ").lower()
        if choice3 == "f":
            print("")
            print("🚪___﹏﹏﹏﹏🏊🏽🐡🐡🐡🐡🐡🐡🐡🐡🐡﹏﹏﹏﹏﹏﹏﹏")
            print("It's a room full of Piranhas, GameOver")
        elif choice3 == "m":
            print("")
            print("🚪___________🚶🏽‍♂️‍➡️_✨👑⚱️💎✨__________________")
            print("You found the treasure. You Win!")
        elif choice3 == "s":
            print("")
            print("🚪___________🚶🏽‍♂️‍➡️🐍🐍🐍🐍🐍🐍🐍🐍🐍___________")
            print("You enter a room full of snakes, GameOver.")
        else:
            print("")
            print("🚪___🤷🏻___")
            print("You chose a door that doesn't exist. GameOver.")

    elif choice2 == "s":
        print("")
        print("🚪___﹏﹏﹏﹏🏊🏽🐊🐊🐊🐊🐊🐊🐊🐊🐊﹏﹏﹏﹏﹏﹏﹏")
        print("You got attacked by crocs, GameOver.")
    else:
        print("")
        print("___🤷🏻___")
        print("Invalid Option. GameOver.")

elif choice1 == "l":
    print("")
    print("____                       _________________")
    print("    |_________🧎🏻__________|")
    print("You fall into an old well, GameOver.")
else:
    print("")
    print("___🤷🏻___")
    print("Invalid Option. GameOver.")
