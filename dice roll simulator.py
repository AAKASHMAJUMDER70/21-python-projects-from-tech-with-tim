def dice_roll_num_gen():  
    import random 
    num_gen = random.randint(1,6)
    return num_gen

user_input = int(input("Enter the number of times you want to roll the dice: "))
c=0
num = []
while c<user_input :
    c+=1
    num.append(dice_roll_num_gen())
    
print(f"the dice was rolled {user_input} times and number generated were {num} ")
    