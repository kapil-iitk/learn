# Exercise 1.10
# Author: Noah Waterfield Price

from math import pi, exp, sqrt

m = 0
s = 2.0
x = 1.0

f = (1 / (s*sqrt(2 * pi))) * exp(-0.5 * ((x - m) / s) ** 2)
print f

"""
Sample run:
python Gaussian1.py
0.352065326764
"""
