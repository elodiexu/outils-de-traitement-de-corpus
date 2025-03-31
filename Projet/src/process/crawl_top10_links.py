import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

BASE_URL = "https://www.allocine.fr"

def get_top10_links(year):
    url = f"https://www.allocine.fr/film/meilleurs/annee-{year}/"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    film_blocks = soup.find_all('li', class_='mdl')[:10]
    for film in film_blocks:
        a_tag = film.find('a', href=True)
        if a_tag:
            film_url = BASE_URL + a_tag['href']
            links.append(film_url)
    return links

def main():
    for year in [2022, 2023, 2024]:
        print(f"Année {year} :")
        top_links = get_top10_links(year)
        for link in top_links:
            print(link)
        print("\n")

if __name__ == "__main__":
    main()