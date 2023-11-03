a=float(input("Enter the 1st Number: "))
b=float(input("Enter the 2nd Number: "))
opr=str(input("Enter the opertor: "))

if opr=="+":
    print(a+b)
elif opr=="-":
    print(a-b)    
elif opr=="*":
    print(a*b) 
elif opr=="/":
    print(a/b)
elif opr=="**":
    print(a**b)
else:
    print("Invalied")