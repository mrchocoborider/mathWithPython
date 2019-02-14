'''
Calculating the mode
'''

from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

'''
Frequency table
'''

def frequency_table(numbers):
    table = Counter(numbers)
    print ('Number\tFrequency')
    numbers_freq = table.most_common()
    numbers_freq.sort()

    for number in numbers_freq:
        print('{0}\t{1}'.format(number[0], number[1]))


if __name__ == '__main__':

    print('Press 1 for modes, 2 for a frequency table')
    a = input('1 or 2? ')
    if a == '1':
        scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
        modes = calculate_mode(scores)

        print('The mode(s) of the list of numbers is/are: ')
        for mode in modes:
            print(mode)
    elif a == '2':
        scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
        frequency_table(scores)
    else:
        print('Please choose 1 or 2')


