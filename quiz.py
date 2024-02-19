import re
print("Welcome to my computers quiz game!")

playing = input("Do you want to play? Reply Yes/No.")
score = 0
pos = re.compile(r"(?i)yes")
neg = re.compile(r"(?i)no")

if pos.match(playing):
    print ("Ok. Let's continue with the game. ")
else:
    print("Have a nice day.Goodbye!")
    quit()
    
print("There is a set of 20 questions about data science. 1 mark for each correct answer and 0 for incorrect. No negative marking.")
print("Wishing you All The Best!")
print("Starting in: ")
print("1")
print("2")
print("3")

answer = input("What is SQL?")
ans1 = "Structured Query Language"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")

    
answer = input("What is TLS?")
ans1 = "Transport Layer Security"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is API?")
ans1 = "Application Programming Interface"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is SSL?")
ans1 = "Secure Sockets Layer"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is URL?")
ans1 = "Uniform Resource Locator"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is XML?")
ans1 = "eXtensible Markup Language"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is JSON?")
ans1 = "JavaScript Object Notation"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is CSS?")
ans1 = "Cascading Style Sheets"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is HTML?")
ans1 = "Hyper Text Markup Language"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is PCA?")
ans1 = "Principal Component Analysis"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is RNN?")
ans1 = "Recurrent Neural Network"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is CNN?")
ans1 = "Convolution Neural Network"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is ANN?")
ans1 = "Artificial Neural Network"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is KNN?")
ans1 = "K Nearest Neighbour"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is SVM?")
ans1 = "Support Vector Machine"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is EDA?")
ans1 = "Exploratory Data Analysis"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is DL?")
ans1 = "Deep Learning"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is NLP?")
ans1 = "Natural Language Processing"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is AI?")
ans1 = "Artificial Intelligence"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")


answer = input("What is ML?")
ans1 = "Machine Learning"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
    score+=1
else:
    print("The answer is incorrect.")
    
perc = (score/20)*100 
print("You have successfully completed the quiz.")
print(f"Your score of the quiz is {score} and {perc}%")