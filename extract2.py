import requests
from bs4 import BeautifulSoup

# Fetch the web page content
url = "https://www.notion.so/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the HTML code without inline CSS
html_code = ""
for element in soup.find_all():
    if element.name in ['style']:
        continue
    html_code += str(element)

print(html_code)