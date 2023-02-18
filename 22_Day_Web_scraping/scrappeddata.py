import requests

from bs4 import BeautifulSoup
url = 'https://andrew4779.github.io/Plio/'

response = requests.get(url)
status = response.status_code
print(status) 


import requests
from bs4 import BeautifulSoup

url = "https://moringaschool.com/"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)