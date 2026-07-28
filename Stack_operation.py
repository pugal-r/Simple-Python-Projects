#stack operation

stack=[]

def push():
    item=int(input("Enter the Push Element:"))
    stack.append(item)
    print(item,"Pushed into a Stack")
    print(stack)

def pop():
    if len(stack) == 0:
        print("Stack Overflow")
    else:
        print("Popped Element is :",stack.pop())
    print(stack)

def peek():
    if len(stack)==0:
        print("Stack is Empty")
    else:
        print("Top Element is:",stack[-1])

def dispay():
    if len(stack)==0:
        print("Stack is Empty")
    else:
        print("Stack Elements are:",stack)
    

while True:
    print("------Stack Operation------")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display Stack")
    print("5.Exit")

    choice=int(input("Enter the Stack Operation:"))

    if choice == 1:
        push()
    elif choice ==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        dispay()
    elif choice==5:
        break


