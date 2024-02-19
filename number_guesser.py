import random

print("Welcome to the number guessing game.")
print("You have to provide a starting point and the ending point(inclusive) of the range within which you will guess the number ")
print("Let's begin the game.")

starting = input("Enter the lower range of the range in which you want to guess the number. ")
ending = input("Enter the upper range of the range in which you want to guess the number. ")
num_from_user_side = input("Enter the number which you want to guess. ")


if starting.isdigit() and ending.isdigit() and num_from_user_side.isdigit():
    pass
else:
    print("You might have entered a non integer value in atleast one input.")
    quit()



num_generated_by_code = random.randint(int(starting),int(ending))

def check_the_guessed_num(number):
    if num_generated_by_code==number:
        return True     
    else:
        return False     


if check_the_guessed_num(int(num_from_user_side))==True:
    print(f"Congratuations! You have guessed the correct number {num_from_user_side}.")
else:
    print(f"Bummer! You made an incorrect guess.")
    
    

    
    
          






























































