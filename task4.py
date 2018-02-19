# 3.14 looks like a 'magic number'. Use var to explain value in future.
import math
R = input('Enter the radius of the circle: ')
S = math.pi * (int(R) ** 2)
print('S =', S)
