
#Calculator operations 

print("--Calculate for the 2 numbers--")
a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
print("---Select The operation---")
print("1.Addition")
print("2.subtraction")
print("3.Multiply")
print("4.Division")
print("5.Floor Division")
print("6.square root")

choice=int(input("Select One Operation :"))

if choice==1:
    add=a+b
    print(f"Addition of {a} and {b} is :",add)
elif choice==2:
    sub=a-b
    print(f"Subtraction of {a} and {b} is :",sub)
elif choice==3:
    mul=a*b
    print(f"Multiple of {a} and {b} is :",mul)
elif choice==4:
    div=a/b
    print(f"Division  of {a} and {b} is :",div)
elif choice==5:
    fdiv=a//b
    print(f"Floor Division  of {a} and {b} is :",fdiv)
elif choice==6:
    smul=a**b
    print(f"square root  of {a} and {b} is :",smul)
else:
    print("---Invalid Choice--")