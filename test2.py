import math
import numpy

def f(x):
    return math.log(x,math.e) + 2 * math.cos(x)

# Implementing False Position Method
def falsePosition(x0,x1,e=0.1**(20)):
    tablica_x = []
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.10f and f(x2) = %0.10f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        tablica_x.append(x0)
        tablica_x.append(x2)
        step = step + 1
        condition = abs(f(tablica_x[-1])-f(tablica_x[-2])) > e

    print('\nRequired root is: %0.10f' % x2)


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
#e = input('Tolerable Error: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
#e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,)#e)