'''
Fraction operations
'''
from fractions import Fraction

def add(a, b):
    print('Result of Addition: {0}'.format(a+b))

def sub(a, b):
    print('Result of Subtraction: {0}'.format(a-b))

def div(a, b):
    print('Result of Division: {0}'.format(a/b))

def mult(a, b):
    print('Result of Multiplication: {0}'.format(a*b))


if __name__ == '__main__':
    while True:
        try:
            a = Fraction(input('Enter first fraction: '))
        except ZeroDivisionError:
            print("You know you shouldn't do that")
            exit()
        try:
            b = Fraction(input('Enter second fraction: '))
        
        except ZeroDivisionError:
            print("You know you shouldn't do that")
            exit()
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        if op == 'Add':
            add(a, b)
        elif op == 'Subtract':
            sub(a, b)
        elif op == 'Divide':
            div(a, b)
        elif op == 'Multiply':
            mult(a, b)
        else:
            print('Please enter a valid operation.')
        answer = input('Do you want to exit? (y/n)')
        if answer == 'y':
            break
