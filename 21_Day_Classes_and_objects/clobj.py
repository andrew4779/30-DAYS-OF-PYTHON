# class person:
#     pass
# print(person)

# p = person
# print(p)


# Use the __int__ constructor
class person:
    def __init__(self, name):
        self.name = name

# pp
class Student(person):
    def __init__(self, firstname = "Andrew", lastname = "kimani", age = 20, country = "Kenya", city = "Nairobi", gender = "male"):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'she'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)
