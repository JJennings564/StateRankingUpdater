import requests
from bs4 import BeautifulSoup

r = requests.get('https://osuworld.octo.moe/')

print(r)

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='leaflet-pane leaflet-overlay-pane')
if s:
    s2 = s.find('svg', class_='leaflet-zoom-animated')
    if s2:
        contents = s2.find_all('g')
        print(contents)
    else:
        print("No element with class 'leaflet-zoom-animated' found.")
else:
    print("No element with class 'leaflet-pane leaflet-overlay-pane' found.")