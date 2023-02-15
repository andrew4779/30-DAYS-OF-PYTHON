# def greet_person(firstname, lastname):
#     return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'


# import webbrowser

# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/drew-kimani/',
#     'https://github.com/andrew4779',
#     'https://twitter.com/masaneii',
# ]

# for url in url_lists:
#     webbrowser.open_new_tab(url)

# API- Application program interface
# To open a network connection you need a package  called _requests_


import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)
