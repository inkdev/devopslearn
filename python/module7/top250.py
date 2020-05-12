import requests
import json
from bs4 import BeautifulSoup

def parse_top_250(json_file):
    url = 'https://imdb.com/chart/top'
    parse = requests.get(url, headers={'Accept-Language': 'En-us'})
    soup = BeautifulSoup(parse.text, features="lxml")
    film_list = []
    for frame in soup.tbody.find_all('tr'):
        title = frame.find('td', class_='titleColumn').a.text
        chart = frame.find('td', class_='posterColumn').span['data-value']
        year = frame.find('td', class_='titleColumn').span.text.strip('()')
        act = frame.find('td', class_='titleColumn').a['title'].split(', ')
        rate = frame.find('td', class_='ratingColumn imdbRating').strong.text
        film = {
            title: {
                'Position': chart,
                'Year': year,
                'Director': act[0].strip(' (dir.)'),
                'Crew': f'{act[1]}, {act[2]}',
                'Rating': rate
            }
        }
        film_list.append(film)
    with open(json_file, 'w') as f_write:
        json.dump(film_list, f_write, indent=4)

#parse_top_250('output.json')