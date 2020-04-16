class SimplyCal:

    x = float(input('Enter your first number: '))
    y = float(input('Enter your second number: '))

    operation = input( ' Please type in the math operation you would like to complete:'
                      ' + addition'
                       ' - subtraction'
                       ' * mulitply'
                       ' / division ''')

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply (x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            raise ValueError('Can not divide by zero')
        return x / y

    if operation == '+':
        print(add(x,y))

    elif operation == '-':
        print(subtract(x,y))

    elif operation == '*':
        print (multiply(x, y))

    elif operation == '/':
        print(divide(x, y))

    else:
        print("Invalid input")

