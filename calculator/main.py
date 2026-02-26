try:
    a = int(input("enter a number"))
    b = int(input("enter a number "))
    print("what kind of operation do you want to perform. Press + for addition\nPress - for subtraction\nPress / for division\npress * for multiplication")
    O = input("Enter Operation: ")
    match o:
        case "+":
            print(f"the sum is: {a + b}")
        case "-":
            print(f"the sum is: {a - b}")
        case "*":
            print(f"the sum is: {a * b}")
        case "/":
            print(f"the sum is: {a / b}")
        case _:
            print("invalid operation")
except Exception as e:
    print(e)
