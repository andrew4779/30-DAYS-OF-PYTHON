# class person:
#     pass
# print(person)

# p = person
# print(p)


# Use the __int__ constructor
class person:
    def __init__(self, name):
        self.name = name

p = person('Andrew')
print(p.name)
print(p)