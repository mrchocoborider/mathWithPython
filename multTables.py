'''
Multiplication table printer
'''

#Enhanced: before it was the number and ten multiples, 
#now you can pick the # of multiples you'd like to see
def multi_table(a, b):
    
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))


if __name__ == '__main__':
    #exit power to the user!
    while True:
        a = input('Enter a number: ')
        b = float(input("Enter the number (integer) of multiples you'd like: "))
        if b.is_integer():
            multi_table(float(a), int(b))
            answer = input('Do you want to exit? (y/n)')
            if answer == 'y':
                break
        else:
            print('Please enter an integer for the number of multiples.')    
