print("This is the program for a simple acronym creator from a supplied piece of string")

user_string  = input("Enter the string from which you want to create an acronym: ") 

list_of_substring = user_string.split()
acronym = ""

for i in list_of_substring:
    acronym += i[0].upper()
    
print(acronym)
    