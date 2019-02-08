'''
Even Odd Vending Machine
Print whether the number is even, display the number
followed by the next 9 even or odd numbers.
'''

def evenOdd(a):
    if a % 2 == 0:
        b = ', '.join([str(a + i) for i in range(2, 20, 2)])
        text = 'Even {}, {}'.format(a, b)
        print(text)

    else:
        b = ', '.join([str(a + i) for i in range(2, 20, 2)])
        text = 'Odd {}, {}'.format(a, b)
        print(text)


if __name__ == '__main__':
    while True:
        a = float(input('Enter an integer '))
        
        if a.is_integer():
            a = int(a)
            evenOdd(a)
        else:
            print('Please enter an integer ')
        answer = input('Do you want to exit? (y/n)')
        if answer == 'y':
            break

