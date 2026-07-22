print("Arithmetic operations: ")
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
need=int(input("Enter the operation number (1:+, 2:-, 3:*, 4:/): "))
match need:
    case 1:
        operation='+'
    case 2:
        operation='-'
    case 3:
        operation='*'
    case 4:
        operation='/'
    case _:
        operation=''
        print("Invalid, please enter a valid number between 1 and 4")


if operation!='':
    if operation=='+':
        print("Addition: ", a+b)
    elif operation=='-':
        print("Subtraction: ", a-b)
    elif operation=='*':
        print("Multiplication: ", a*b)
    elif operation=='/':
        print("Division: ", a/b)
else:
    print("Not a valid operation")
