import requests
from bs4 import BeautifulSoup
import utilities as u

url = 'https://www.health.state.mn.us/facilities/providers/doula/registry.html'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

filter_1 = soup.find_all('div', class_='field field--name-body field--type-text-with-summary field--label-hidden')
# Filter to the third index of the given class
filter_2 = filter_1[3] 

# Filter through all the entries
filter_3 = filter_2.find_all('p')
for entry in filter_3:
    strong_tags = entry.find_all('strong')
    
    if strong_tags:
        # Name
        possible_name = strong_tags[0].text
        if ',' in possible_name:
            # Stored in possible_name var
            pass