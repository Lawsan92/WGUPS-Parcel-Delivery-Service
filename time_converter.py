import math

def time_converter(miles):
    mph = 18
    return math.ceil((miles / mph) * 60)

print(time_converter(2.0))