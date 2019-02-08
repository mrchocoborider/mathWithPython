'''
Unit converter: Miles and Kilometers
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

def kilo_lbs():
    kilos = float(input('Enter weight in kilograms: '))
    lbs = kilos * 2.2

    print('Weight in pounds: {0}'.format(lbs))

def lbs_kilo():
    lbs = float(input('Enter weight in pounds: '))
    kilos = lbs/2.2

    print('Weight in kilos: {0}'.format(kilos))

if __name__ == '__main__':
    while True:
        print_menu()
        choice = input('Which conversion would you like to do?: ')
        if choice == '1':
            km_miles()

        if choice == '2':
            miles_km()

        if choice == '3':
            kilo_lbs()

        if choice == '4':
            lbs_kilo()

        answer = input('Do you want to exit? (y/n)')
        if answer == 'y':
            break