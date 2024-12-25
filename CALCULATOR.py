from calculator_art import art

print(art)

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    accumulate = True
    n1 = float(input('Enter first number: '))


    while accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation: ')
        n2 = float(input('Enter second number: '))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1}{operation_symbol}{n2} = {answer}")

        choice = input('Do you want to do another operation with this number? (y/n): ')
        if choice == 'y':
            n1 = answer
        else:
            accumulate = False
            print("\n" * 20)
            calculator()




