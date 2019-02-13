'''
Barchart of weekly expenditures
'''
import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
    # Number of bars
    num_bars = len(data)
    # This list is the point on the y-axis where each
    # Bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title('Weekly expenditures')
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()

if __name__ == '__main__':
    try:
        #number of categories
        ncat = int(input('Enter the number of categories: '))
        cats = []
        amts = []
        for i in range(1, ncat+1):
            cat = input('Enter category: ')
            amt = float(input('Expenditure: '))
            cats.append(cat)
            amts.append(amt)
    except ValueError:
        print('Enter a valid number of categories')
    else:
        create_bar_chart(amts, cats)
