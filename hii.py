# def area_by_shoelace(x, y):
#     "Assumes x,y points go around the polygon in one direction"
#     return abs( sum(i * j for i, j in zip(x, y[1:])) + x[-1] * y[0]
#                -sum(i * j for i, j in zip(x[1:], y)) - x[0] * y[-1]) / 2


'''
File: return_with_nested_cond_exprs.py
Purpose: Demonstrate nested conditional expressions used in a return statement,
to classify letters in a string as lowercase, uppercase or neither.
Also demonstrates doing the same task without a function and a return,
using a lambda and map instead.
Author: Vasudev Ram
Copyright 2017 Vasudev Ram
Web site: https://vasudevram.github.io
Blog: https://jugad2.blogspot.com
'''

from __future__ import print_function
from string import lowercase, uppercase

# Use return with nested conditional expressions inside a function,
# to classify characters in a string as lowercase, uppercase or neither:
def classify_char(ch):
    return ch + ': ' + ('lowercase' if ch in lowercase else \
    'uppercase' if ch in uppercase else 'neither')

print("Classify using a function:")
for ch in 'AaBbCc12+-':
    print(classify_char(ch))

print()

# Do it using map and lambda instead of def and for:
print("Classify using map and lambda:")

print('\n'.join(map(lambda ch: ch + ': ' + ('lowercase' if ch in lowercase else
'uppercase' if ch in uppercase else 'neither'), 'AaBbCc12+-')))
