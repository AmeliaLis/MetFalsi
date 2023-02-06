MAX_ITER = 100
import math


def func(x):
    return (math.log(x,math.e) + 2 * math.cos(x))

# Prints root of func(x) in interval [a, b]


def regulaFalsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result
    k=0
    while c!=0 and k!=MAX_ITER:
        k+=1
        # Find the point that touches x axis
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        print(c)
        print(k)

        # Check if the above found point is root
        #if func(c) == 0:
        #    print("c is equal to 0")
         #   break

        # Decide the side to repeat the steps
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : ", '%.15f' % c)


# Driver code to test above function
# Initial values assumed
a = 1
b = 3
regulaFalsi(a, b)
