import art


# 4 functions - addition, subtract, multiply and divided.
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divided(n1, n2):
    return n1 / n2


# adding 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divided

}
# performinng calculations


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number: "))
    calculation_steps = []   # ← store all steps

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an operation: ")
        if operations_symbol not in ["+", "-", "*", "/"]:
            print("Invalid operation pick correct operation")
            continue

        num2 = float(input("What is the next number:? "))
        answer = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        step = f"{num1} {operations_symbol} {num2} = {answer}"
        calculation_steps.append(step)   # ← save the step
        print(step)

# restart logic
        while True:
            choice = input(f"""Type 'yes' or 'y' to continue calculating {answer} or 
type 'no' or 'n' to start a new calculation or 
type 'Exit' or 'e' to Close the calculation """).lower()

            if choice in ['yes', 'y']:
                num1 = answer
                break
            elif choice in ['no', 'n']:
                should_accumulate = False
                print("\n" * 20)
                calculator()
                break
            elif choice in ['exit', 'e']:
                print("\nFull Calculation History:")
                for s in calculation_steps:
                    print(s)
                print(f"\nFinal result is {answer}")
                return
            else:
                print("Invalid option. Please type yes/y or no/n.")


calculator()
