import requests
from bs4 import BeautifulSoup

website_url = "https://www.notion.so/"
host = "https://www.notion.so/"

response = requests.get(website_url)

soup = BeautifulSoup(response.content, 'html.parser')

html_file = soup.prettify()

# Extract the HTML code without inline CSS
html_code = ""
for element in soup.find_all():
    if element.name in ['style']:
        continue
    html_code += str(element)

with open('index.html', 'wb') as f:
    f.write(html_file.encode('utf-8'))
