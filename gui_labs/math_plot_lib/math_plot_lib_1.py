from numpy import *
import matplotlib.pyplot as plt
import math

def f(x):
    return (-5*cos(10*x)*sin(3*x))/x**(1/2)

x=linspace(1,10,250)

plt.plot(x,f(x),label='(-5*cos(10*x)*sin(3*x))/x**(1/2)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
