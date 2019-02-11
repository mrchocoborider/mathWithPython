'''
Quadratic function calculator
'''
import matplotlib.pyplot as plt


# Assume values of x
x_values = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
y_values = []
for x in x_values:
    # Calculate the value of the quadratic function
    y = x**2 + 2*x +1
    y_values.append(y)
    #print('x={0} y={1}'.format(x, y))

plt.plot(x_values, y_values)
plt.show()

