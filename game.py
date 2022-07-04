#Game made by Derias => https://github.com/Derias20
#Game is bugging after three rounds, Im going to make a fixing update later.
import random
while True:
    possible_choices = ["rock" , "paper" , "scissors"]
    player_choice = input("Hello!\nChoose your item: rock , paper or scissors \n")
    computer_choice = random.choice(possible_choices)
    print("computer choosen:"+ " " + computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
         print("You won!")
        else:
         print("You lost.")
    elif player_choice == "paper":
        if computer_choice == "rock":
         print("You won!")
    else:
        print("You lost.")
    if player_choice == "scissors":
        if computer_choice == "paper":
         print("You won!")
        else:
         print("You lost.")
    play_again = input("Another game? (y/n): ")
    if play_again.lower() != "y":
     break
