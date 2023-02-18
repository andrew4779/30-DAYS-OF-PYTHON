import requests

from bs4 import BeautifulSoup
url = 'https://andrew4779.github.io/Plio/'

response = requests.get(url)
status = response.status_code
print(status)