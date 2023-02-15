# def greet_person(firstname, lastname):
#     return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'


import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/drew-kimani/',
    'https://github.com/andrew4779',
    'https://twitter.com/masaneii',
]

for url in url_lists:
    webbrowser.open_new_tab(url)