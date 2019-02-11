'''
Enhanced Projectile motion calculator
'''

'''
Generate equally spaced floating 
point numbers between two given values
'''

def frange(start, final, increment):

    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers

'''
Draw the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')


def draw_trajectory(u, theta, i):
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    print('Flight time for trajectory {0}: {1}'.format(i, t_flight))
    # Find time intervals
    intervals = frange(0, t_flight, 0.001)

    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    print('Maximum vertical distance traveled for trajectory {0}: {1}'.format(i, max(y)))
    print('Maximum horizontal distance traveled for trajectory {0}: {1}'.format(i, max(x)))

    draw_graph(x, y)

if __name__== '__main__':

    #User input, multiple trajectories
    try:
        trajs = float(input('How many trajectories? '))
        vna = []
        for i in range(1, int(trajs)+1):
            v = float(input('Enter the initial velocity for trajectory {} (m/s): '.format(i)))
            a = float(input('Enter the initial angle for trajectory {} (degrees): '.format(i)))
            vna.append([v, a, i])
    except ValueError:
        print('You entered an invalid input')
    else:
        leg = []
        for v in vna:
            draw_trajectory(v[0], v[1], v[2])
            leg.append(v[0])
        plt.legend(leg)
        plt.show()





