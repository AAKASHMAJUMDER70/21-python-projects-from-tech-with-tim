import random

print("Welcome to the number guessing game.")
print("You have to provide a starting point and the ending point(inclusive) of the range within which you will guess the number ")
print("Let's begin the game.")

starting = int(input("Enter the lower range of the range in which you want to guess the number. "))
ending = int(input("Enter the upper range of the range in which you want to guess the number. "))
num_from_user_side = int(input("Enter the number which you want to guess. "))
num_generated_by_code = random.randint(starting,ending)

def check_the_guessed_num(number):
    if num_generated_by_code==number:
        return True     
    else:
        return False     

if isinstance(starting, int) and isinstance(ending, int) and isinstance(num_from_user_side, int):
    pass
else:
    print("You might have entered a non integer value in atleast one input.")
    quit()

if check_the_guessed_num(num_from_user_side)==True:
    print(f"Congratuations! You have guessed the correct number {num_from_user_side}.")
else:
    print(f"Bummer! You made an incorrect guess.")
    
    

    
    
          






























































