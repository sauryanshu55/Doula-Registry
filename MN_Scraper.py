import requests
from bs4 import BeautifulSoup
import utilities

url = 'https://www.health.state.mn.us/facilities/providers/doula/registry.html'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
divs = soup.find_all('div', class_='field field--name-body field--type-text-with-summary field--label-hidden')

for div in divs:
    utilities.write_to_scratch(div.prettify(), False)


