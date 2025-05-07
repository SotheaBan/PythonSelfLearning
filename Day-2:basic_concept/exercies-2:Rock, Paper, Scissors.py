# Tags: list, range, random, input, print
# This is a popular hand game played between two people. Each player gets to form one of three shapes using their hand:
# rock (a closed fist)
# paper (a flat hand)
# scissors (a fist with the index finger and middle finger extended, forming a V)

import random 

items = ["rock","paper","scissors"]
print("Welcome to game !")
while True: 
    computer= random.choice(items)
    person = input("enter choice : ")

    if computer == person : 
        print("drew ! ")

    elif computer== "rock": 
        if person == 'paper': 
            print(computer)
            print("you win")
        else: 
            print("you Lose")

    elif computer == "paper": 
        if person == 'rock': 
            print(computer)
            print("you Lose")
        else: 
            print("you Win")
    elif computer == "scissors": 
        if person == 'rock': 
            print(computer)
            print("you Lose")
        else: 
            print("you Win")
    else: 
        print("Error Input")
    
