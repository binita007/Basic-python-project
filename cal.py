# make a calculator using python
a=int(input("enter the first number : "))
b=int(input ("enter the second number : "))
op=input("enter the operation would you like to perform (+, -, *, /): ")
sum=a+b
sub=a-b
mul=a*b
div=a/b
if op== "+":
    print("The summation of",a,"and",b,"is",sum)
elif op=="-":
    print("The subtraction of",a,"and",b,"is",sub)
elif op=="*":
    print("The multiplication of",a ,"and",b ,"is",mul)
elif op=="/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("The divisible value of ",a ,"and",b,"is",div)
else:
    print("Invalid operation")












