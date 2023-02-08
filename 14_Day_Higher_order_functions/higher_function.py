def sum_numbers(nums):
    return sum(nums)


def higher_order_function(f, lst):
    summation = f(lst)
    return summation

#    /////////////////////////////////////////////////
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)

def square(x):
    return(x ** 2)

def cube(x):
    return(x ** 3)

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type =='absolute':
        return absolute

result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result = higher_order_function('absolute')
print(result(-3))

# A decorator is a design pattern in python which allows a user to add a new functionality to an object without modifying its structure.

def greeting():
    return 'Welcome to python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())