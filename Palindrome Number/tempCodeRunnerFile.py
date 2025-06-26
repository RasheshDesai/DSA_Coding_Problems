import math

def mySqrt(x):
    square_root = math.sqrt(x)
    nearest_integer = round(square_root)
    return nearest_integer
print(mySqrt(x=4))