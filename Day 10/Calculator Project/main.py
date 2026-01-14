def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
Continue_Calculating = True
Restart_with_result=False
output = 0
while Continue_Calculating:
    if Restart_with_result:
        n1=output
    else:
        n1=float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    user_operation = input("Pick an operation: ")
    n2=float(input("Enter the second number: "))
    output = operations[user_operation](n1, n2)
    print(f"The result is: {n1} {user_operation} {n2}= {output}")
    user_operation = input("Continue calculating with result? (y/n): ")
    if user_operation == "y":
        Restart_with_result=True
    else:
        Restart_with_result=False
        user_operation = input("Continue with calculating or abort? (y/a): ")
        if user_operation == "y":
            Continue_Calculating = True
        else:
            Continue_Calculating = False