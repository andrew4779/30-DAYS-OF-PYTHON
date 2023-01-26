# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# else:
#     print(count)




# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)
# # 


# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers:
#     print(numbers)


# language = 'python'
# for letter in language:
#     print(language)

# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers:
#     print(numbers)

person = {
    'first_name':'Andrew',
    'last_name':'kimani',
    'age':250,
    'country':'Kenya',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out


lst = list(range(11))
print(lst)
st = set(range(1,11))
print(st)


