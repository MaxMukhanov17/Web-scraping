import requests
import bs4

KEYWORDS = ['Процессоры', 'Удалённая работа', 'web', 'Python']
URL = 'https://habr.com/ru/all/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70'}

response = requests.get(url=URL, headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip(' *') for hub in hubs)
    for hub in hubs:
        if hub in KEYWORDS:
            date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
            title = article.find(class_='tm-article-snippet__title-link').text
            url_post =URL.strip('/ru/all/') + article.find(class_='tm-article-snippet__title-link').attrs['href']
            print(f'{date} - {title} - {url_post}')
            resp = requests.get(url=url_post).text
            text_article = soup.find_all('p')
            # print(text_article)