import requests
from bs4 import BeautifulSoup
import utils.utilities as util

is_parsed = True # Set to True, if already parsed.
soup = None

if not is_parsed:
    url = 'https://www.health.state.mn.us/facilities/providers/doula/registry.html'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
else:
    with open('scrapers/content/mn.txt', 'r') as html_content:
        soup = BeautifulSoup(html_content.read(), 'html.parser')

filter_1 = soup.find_all('div', class_='field field--name-body field--type-text-with-summary field--label-hidden')

# Filter to the third index of the given class
filter_2 = filter_1[3] 

# Filter through all the entries
filter_3 = filter_2.find_all('p')

for entry in filter_3[3:]:
    
    # Extract Names
    name = entry.find('strong')
    if name:
        name = name.get_text(strip = True)