import random

cnumber=random.randrange(1,50)
userinput=int(input("enter your guess number : "))

if cnumber>userinput:
    print("computer guess number is ",cnumber)
    print("Your guess number is too low !!!")
elif cnumber<userinput:
    print("computer guess number is ",cnumber)
    print("Your guess number is too high !!!")
else:
    print("computer guess number is ",cnumber)
    print("Congratulations Your guess is correct !!!!")