import random
words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry", "blueberry", "watermelon", "kiwi", "mango","apple", "banana", "orange","book", "pen", "pencil", "paper","tree", "flower", "grass", "sunflower","tree", "flower", "grass", "sunflower","car", "bicycle", "train", "plane"]
num_of_lists_to_be_generated = int(input("Enter the number of lists to be generated: "))
min_words = int(input("Enter the minimum number of words of the words in lists to be generated: "))
max_words = int(input("Enter the maximum number of words of the words in lists to be generated: "))
for i in range(num_of_lists_to_be_generated+1): 
    num_of_words = random.randint(min_words,max_words)
    word_list  = random.sample(words,num_of_words)
    print(f"the word list of {i}th number is {word_list}") 
     