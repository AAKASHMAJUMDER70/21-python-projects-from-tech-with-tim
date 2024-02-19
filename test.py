import re
answer = input("What is SQL?")
ans1 = "Structured Query Language"
pattern = re.compile(f"(?i){ans1}")
if pattern.fullmatch(answer):
    print("The answer is correct.")
else:
    print("The answer is incorrect.")
