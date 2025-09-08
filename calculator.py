from mymath import sub as s, add
while True:
    print("Hello and welcome to the calculator, please select an option!\n1. add\n2. sub")
    res = input("Please choose an option: ")
    try:
        if res not in "12" or res == '':
            raise Exception
        res = int(res)
    except:
        print("The number is invalid try again.")
        continue

    if res == 1:
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        
        try:
            x = int(x)
            y = int(y)
        except:
            print("First or second number is invalid, Please try again :(")

        print(f"Result: {add(x, y)}")
    else:
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        
        try:
            x = int(x)
            y = int(y)
        except:
            print("First or second number is invalid, Please try again :(")

        print(f"Result: {s(x, y)}")
    
    print("Thank you for trying my program!\n\n")


