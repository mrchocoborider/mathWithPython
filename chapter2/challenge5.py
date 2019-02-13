'''
Graph the ratio between
consecutive Fibonacci numbers
'''
import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c

    return series


fibnumbers = fibo(98)

x_numbers = range(1, len(fibnumbers)+1)
y_numbers = []
for i in range(len(fibnumbers)):
    if i == 0:
        y_numbers.append(1)
    else:
        r = fibnumbers[i] / fibnumbers[i-1]
        y_numbers.append(r)

plt.plot(x_numbers, y_numbers)
plt.xlabel('Ratio')
plt.ylabel('No.')
plt.title('Ratio between consecutive Fibonacci numbers')
plt.xlim(0, 100)
plt.ylim(1, 2.2)
plt.show()
