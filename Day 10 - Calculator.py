def add(n1, n2):
    """ Add the given two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """ Subtract the given two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """ Multiply the given two numbers"""
    return n1 * n2

def divide(n1, n2):
    """ Divide the given two numbers"""
    return n1 / n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

def new_calculation() :
    num1 = float(input("What is the first number? "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    num2 = float(input("What is the next number: "))
    result = operations[operation](num1,num2)
    print(f'{num1} {operation} {num2} = {result}')
    return result

def continue_calculation(result) :
    num1 = result
    operation = input("+\n-\n*\n/\nPick an operation: ")
    num2 = float(input("What is the next number: "))
    result = operations[operation](num1,num2)
    print(f'{num1} {operation} {num2} = {result}')
    return result

result = new_calculation()

stop_calculator = True
while stop_calculator:
    repeat = input(f'Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ')
    if repeat == 'n':
        result = new_calculation()
    elif repeat == 'y':
        result = continue_calculation(result)
    else :
        stop_calculator = False