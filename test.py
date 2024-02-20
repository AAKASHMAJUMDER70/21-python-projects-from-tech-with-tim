def check_winner(user_chooses=input().lower(),computer_chooses=input().lower()):
    if user_chooses==computer_chooses:
        print("It is a tie")
    elif user_chooses=="rock":
        if computer_chooses=="scissor":
            print("Human Wins")
        elif computer_chooses=="paper":
            print("computer wins")
    elif user_chooses=="paper":
        if computer_chooses=="scissor":
            print("computer Wins")
        elif computer_chooses=="rock":
            print("human wins")
    elif user_chooses=="scissor":
        if computer_chooses=="rock":
            print("computer Wins")
        elif computer_chooses=="paper":
            print("human wins")