from math import *


'''
Write functions in the format shown below, then add them to the "functions" dictionary for them to be graphed.

The value of the functions in the dictionary is the RGB value of the color it will be graphed as. Note, it cannot be (0, 0, 0).
'''


#--------------------------------------------------------------------------------------------------------------------------------#

SCALE = 20

def linear(x, y):

    return x - y

def sqr_root(x, y):

    return sqrt(x)-y

def radical(x, y):

    return x*y - 1

def quadratic(x, y):

    return x**2-y

def poly(x, y):

    return x**3+x**2+x-y

def circle(x, y):

    return x*x + y*y - 50

def full_circle(x, y):

    return y*y + x*x <= 50

def squircles(x, y):

    return sin(x)+cos(y) - .1

def spam(x, y):

    return sin(cos(tan(x)) + sin(cos(tan(y)))) - sin(cos(tan(x*y)))

def golden_ratio(x, y):

    r = sqrt(x*x + y*y)
    theta = atan2(y, x)

    i = 0

    return 1*exp(log(1.618)/(3.14/2)*(theta+6.28*i))-r

functions = {

circle: (0, 255, 0),

}

#--------------------------------------------------------------------------------------------------------------------------------#


#This just gives the scale to the graphing calculator, you should not need to edit this.
def scale():
    return SCALE
#This just gives the dictionary of functions to the graphing calculator, you should not need to edit this.
def get_functions():
    return functions
