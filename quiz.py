# PROJECT 1:
print("Welcome To The Computer Quiz!!!")

question=input("Do You Wanna Play Quiz? ")
if question.lower() =="yes":
    print("Let's play the game")
    score=0
else:
    quit()
    

question=input("Who is the father of computer ? ")
if question.lower()=="charles babbage":
    print("Correct answer")
    score +=1
else:
    print("Incorrect answer")

question=input("What does RAM stands for? ")
if question.lower() =="random access memory":
    print("Correct answer")
    score +=1
else:
    print("Incorrect answer")

question=input("What does ALU stands for ? ")
if question.lower() =="arithmetic and logical unit":
    print("Correct answer")
    score +=1
else:
    print("Incorrect answer")

question=input("How many colors are there in rainbow ? ")
if question.lower() == 7 or "seven":
    print("Correct answer")
    score +=1
else:
    print("Incorrect answer")
    
question=input("The color of sky is ? ")
if question.lower() =="blue":
    print("Correct answer")
    score +=1
else:
    print("Incorrect answer")

question=input("What does CPU stands for ? ")
if question.lower() =="central processing unit":
    print("Correct answer")
    score +=1
else:
    print("Incorrect answer")

print("You got {score} questions correct.")
    