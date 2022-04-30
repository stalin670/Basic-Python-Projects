
#  It's just a basic game that is build through Python Conditional statements
#  You should check it right now and have fun.
#  Just run the code in your terminal and see how exciting it is.


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
print("Your mission is to find the treasure.") 

cross=input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
if cross=="right":
    print("You fell into a hole. Game Over.\n")
else:
    bt=input('You come to lake. There is an island in the middle of the lake. Type "wait" to wait for boat. Type "swim" to swim across.\n')

    if bt=="swim":
        print("You get attacked by an angry trout. Game over.\n")
    else:
        pt=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")

        if pt=='red':
            print("It's a room of full of fire. Game Over.\n")
        elif pt=='blue':
            print("You enter a room of beasts. Game Over.\n")
        elif pt=='yellow':
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
