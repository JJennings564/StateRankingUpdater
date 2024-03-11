import requests
from bs4 import BeautifulSoup

r = requests.get('https://states.osutools.com/states/Oklahoma')

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='players-container')
content = s.find_all_next('h4') + s.find_all_next('h2')

print(content)