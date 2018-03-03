#   A lambda (aka Anonymous Function) is a through away function, that you don't
#   really need a whole function block for
#   Useful in functions that will only be used once and the function is simple.

import math

'''Two Examples to compare normal function and Anonymous function'''
#   Square root function using normal method.
def sqroot(x):
    return math.sqrt(x)

#   Using lambda/anonymous function for same return.
square_rt = lambda x: math.sqrt(x)

print(sqroot(49))
print(square_rt(49))
