from bs4 import BeautifulSoup
import requests

source = requests.get('https://open.spotify.com/').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

# with open('example.html') as html_file:
# 	soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
# match = soup.title.text
# match = soup.div
# match = soup.find('div')
# match = soup.find('div', class_='footer')
# print(match)

# article = soup.find('div', class_='article')
# print(article)

# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)


# for article in soup.find_all('div', class_='article'):
# 	headline = article.h2.a.text
# 	print(headline)

# 	summary = article.p.text
# 	print(summary)
