def sum_numbers(nums):
    return sum(nums)


def higher_order_function(f, lst):
    summation = f(lst)
    return summation

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