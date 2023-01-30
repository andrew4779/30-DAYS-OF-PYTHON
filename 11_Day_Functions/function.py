# # Declaring a function
# def function_name():
#     codes
#     codes
# function_name()



# def generate_full_name():
#     first_name = 'Andrew'
#     last_name = 'kimani'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name

# print(generate_full_name())



def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Andrew'))


def square_number(x):
    return x * x
print(square_number(2))

def subtraction(y):
    return y - 12
print(subtraction(15))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age:', calculate_age(2023, 2002))

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(10, 15))


def find_even_numbers(n):
    evens = []
    for i in range (n + 1):
        if i % 2 ==0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# def find_odd_numbers(a):
#     odds = []
#     for i in range (a+ 1):
#         if i % 3 ==0:
#             odds.append(i)
#     return odds
# print(find_odd_numbers(10))

def greetings (name = "Peter"):
    message = name +" , Welcome to Python everyone!"
    return message
print(greetings())
print(greetings("Andrew"))


def generate_full_name(first_name = "Andrew", last_name = "kimani"):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print (generate_full_name())
print(generate_full_name("David", "Smith"))