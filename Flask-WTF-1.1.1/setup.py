import requests
from bs4 import BeautifulSoup

url = 'https://coding-school.online/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')
for article in articles:
    title = article.find('p').text
    print(title)