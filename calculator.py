# For pratice only
# Calculator Application

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
option = int(input("Enter option from above list: "))
if option not in [1, 2, 3, 4]:
    print("Invalid command")
else:
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))

# Operation
    if option == 1:
        add = num1+num2
        print(f"Addition of {num1}+{num2}={add}")
    elif option == 2:
        sub = num1-num2
        print(f"Subtraction of {num1}-{num2}={sub}")
    elif option == 3:
        sub = num1*num2
        print(f"Multiplication of {num1}*{num2}={sub}")
    elif option == 4:
        sub = num1/num2
        print(f"Division of {num1}/{num2}={sub}")
