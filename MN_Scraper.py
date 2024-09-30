from bs4 import BeautifulSoup
print(BeautifulSoup("<p>This is a test to check Beatiful soup is correctly configured</p>", "html.parser").p.string)

