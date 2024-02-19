import random

def check_the_guessed_num(number):
    if random.randint(2,3) == number:
        print(f"Congratuations! You have guessed the correct number {number}.")     
    else:
        print(f"Bummer! You made an incorrect guess.")     


check_the_guessed_num(2)