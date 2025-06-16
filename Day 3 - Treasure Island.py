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
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your Mission is to find the Treasure.")
input1 = input("You are at the cross road. "
               "Where do you want to go? \n \t "
               "Type 'Left' or 'Right' \n").lower()
if input1 == "left":
    input2 = input("You've come to a lake. "
                   "There is an island in the middle of the lake. \n \t "
                   "Type 'Wait' to wait for the boat. Type 'Swim' to swim across. \n").lower()
    if input2 == "wait":
        input3 = input("You arrived at the island unharmed. "
                       "There is a house with 3 doors. \n \t "
                       "One Red, One Yellow and One Blue. "
                       "Which one do you choose? \n").lower()
        if input3 == "red":
            print("It's Room full of fire. You Lose!!")
        elif input3 == "yellow":
            print("Great! You Won the Treasure!!")
        elif input3 == "blue":
            print("It's Room full of water. You Lose!!")
        else :
            print("Invalid Answer! You Lose!")
    else:
        print("You Got Attacked. You Lose! Game Over!!")
else :
    print("You fell in a hole. You Lose! Game Over!!")