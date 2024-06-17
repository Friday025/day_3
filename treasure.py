print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure....")

choice_1 = input("You're at a crossroad. Where do you want to go? (left or right): ").lower()

if choice_1 == "left":
    choice_2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose? (red/yellow/blue): ").lower()

        if choice_3 == "red":
            print("The room is full of fire. Game Over.....")
        
        elif choice_3 == "yellow":
            print("Congratulations! You found the treasure! You win...")
        
        elif choice_3 == "blue":
            print("You enter a room of beasts. Game Over.....")

        else:
            print("You chose a door that does not exist. Game Over.....")

    elif choice_2 == "swim":
        choice_4 = input("You start swimming across the lake and encounter a school of friendly dolphins. Do you 'follow' them or 'ignore' them? (follow/ignore): ").lower()

        if choice_4 == "follow":
            print("The dolphins guide you safely to the island. You find a hidden path leading to the treasure. You win!")
        else:
            print("You get tired and drown. Game Over.....")
    
    else:
        print("Invalid choice. You get attacked by an angry trout. Game Over.....")

else:
    choice_5 = input("You fell into a hole. Do you want to 'climb' out or 'explore' the hole? (climb/explore): ").lower()

    if choice_5 == "climb":
        print("You climb out safely and continue your journey. However, you get lost in the forest. Game Over.....")
    elif choice_5 == "explore":
        print("You find an underground tunnel that leads you to the treasure. You win!")
    else:
        print("Invalid choice. You remain stuck in the hole. Game Over.....")
