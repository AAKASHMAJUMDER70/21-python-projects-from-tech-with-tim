import random

choices = ["rock","paper","scissor"]

users_choice = input("Choose either rock or paper or scissor: ").lower()
computers_choice = choices[random.randrange(0,3)]


def check_winner(user_chooses,computer_chooses):
    if user_chooses==computer_chooses:
        print("It is a tie")
        return False
    elif user_chooses=="rock":
        if computer_chooses=="scissor":
            print("Human Wins")
            return False
        elif computer_chooses=="paper":
            print("computer wins")
            return False
    elif user_chooses=="paper":
        if computer_chooses=="scissor":
            print("computer Wins")
            return False
        elif computer_chooses=="rock":
            print("human wins")
            return False
    elif user_chooses=="scissor":
        if computer_chooses=="rock":
            print("computer Wins")
            return False
        elif computer_chooses=="paper":
            print("human wins")
            return False

c=0

while c<1:
    c+=1
    if users_choice in choices:
        check_winner(users_choice,computers_choice)
    elif users_choice not in choices:
        print("your input is wrong, please check the spellings or enter the correct choice again.")
        
        
