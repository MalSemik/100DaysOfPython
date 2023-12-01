def calculate():
    first_number = input("Provide first number: ")
    should_continue = True
    while should_continue:
        operation = input("What operation would you like perform? (+, - * /)")
        second_number = input("Provide second number: ")
        result = eval(first_number + operation + second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            first_number = str(result)
        else:
            should_continue = False
            calculate()


calculate()
