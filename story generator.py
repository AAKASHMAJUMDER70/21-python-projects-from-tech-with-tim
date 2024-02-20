print("Welcome to the program where we will generate a story using random module. ")

#program to generate lusts based on your choice 

import random
words1 = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "blueberry", "watermelon", "kiwi", "mango","apple", "banana", "orange","book", "pen", "pencil", "paper","tree", "flower", "grass", "sunflower","tree", "flower", "grass", "sunflower","car", "bicycle", "train", "plane"]
num_of_lists_to_be_generated1 = int(input("Enter the number of lists to be generated: "))
min_words1 = int(input("Enter the minimum number of words of the words in lists to be generated: "))
max_words1 = int(input("Enter the maximum number of words of the words in lists to be generated: "))

def generate_lists(words,num_of_lists_to_be_generated,min_words,max_words):
    lists = []
    
    for i in range(1,num_of_lists_to_be_generated+1): 
        num_of_words = random.randint(min_words,max_words)
        word_list  = random.sample(words,num_of_words)
        lists.append(word_list)
      
    return lists 
        
        
'''#1st way
lists = generate_lists(words1,num_of_lists_to_be_generated1,min_words1,max_words1)
story = ""
for i in lists:
    j = random.randrange(0,len(i))
    story = story + " " + i[j]
print(story)'''

#2nd way
lists = generate_lists(words1,num_of_lists_to_be_generated1,min_words1,max_words1)
story = ""
for i in lists:
    story = story + " " + random.choice(i)
print(story)
        
        
    