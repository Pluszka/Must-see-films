import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
website = response.text

soup = BeautifulSoup(website, 'html.parser')
titles = [title.getText() for title in soup.find_all(name='h3', class_='title')]

with open('List of 100 films.txt', 'w+') as file:
    [file.write(f'{title}\n') for title in titles[::-1]]