# # open('filename', mode)
# f = open('./files/reading_file_example.txt')
# txt = f.read()
# print(type(txt))
# print(txt)
# # print(f)
# f.close()

# f = open('./files/reading_file_example.txt')
# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()



person_dct = {
    "name": "Andrew",
    "country":"Kenya",
    "city":"Nairobi",
    "skills": ["Javascript", "Python", "Angular"]

}

person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"


import json
# JSON
person_json = '''{
    "name": "Andrew",
    "country": "Kenya",
    "city": "Nairobi",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
print(person_dct['city'])
