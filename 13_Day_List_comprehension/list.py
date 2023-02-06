language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

numbers = [i for i in range(11)]
print(numbers)



numbers = [i for i in range (22)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers = [(i, i * i) for i in range(11)]
print(numbers)

def add_two_sums(a,b):
    return  a + b

print(add_two_sums(2, 3))

