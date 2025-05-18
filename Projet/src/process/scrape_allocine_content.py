from bs4 import BeautifulSoup
import requests, time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Étape 1 : récupérer titre via Selenium

def fetch_title(allocine_url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(allocine_url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    title_tag = soup.find("title")
    title = title_tag.text.strip().split("-")[0].strip() if title_tag else "Sans titre"

    driver.quit()
    return title

# Étape 2 : récupérer les critiques via l'API AJAX Allociné

def fetch_reviews(film_id, max_pages=3, max_reviews=5):
    reviews = []
    for page in range(1, max_pages + 1):
        url = f"https://www.allocine.fr/film/fichefilm-{film_id}/critiques/spectateurs/?page={page}&ajax=1"
        r = requests.get(url, headers=HEADERS)

        if r.status_code != 200:
            continue

        soup = BeautifulSoup(r.text, 'html.parser')
        divs = soup.find_all('div', class_='content-txt')

        for div in divs:
            text = div.get_text(separator=" ", strip=True)
            reviews.append(text)

            if len(reviews) >= max_reviews:
                return reviews

        time.sleep(0.3)

    return reviews 

# Étape 3 : sauvegarder le résultat

def save_data_csv(csv_path, year, title, comments, start_id):
    file_exists = os.path.isfile(csv_path)

    with open(csv_path, "a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        
        if not file_exists:
            writer.writerow(["id", "film", "year", "comment"])

        for comment in comments:
            writer.writerow([start_id, title, year, comment])
            start_id += 1

    return start_id
            
# Étape 4 : exécution multi-films avec URLs et IDs

def main():
    csv_path = os.path.join("..", "..", "data", "raw", "all_comments.csv")
    if os.path.exists(csv_path):
        os.remove(csv_path)
    
    global_id = 1
    
    films = {
        "2022": {
            "186636": "https://www.allocine.fr/film/fichefilm_gen_cfilm=186636.html",
            "255726": "https://www.allocine.fr/film/fichefilm_gen_cfilm=255726.html",
            "297895": "https://www.allocine.fr/film/fichefilm_gen_cfilm=297895.html",
            "299413": "https://www.allocine.fr/film/fichefilm_gen_cfilm=299413.html",
            "178014": "https://www.allocine.fr/film/fichefilm_gen_cfilm=178014.html",
            "300250": "https://www.allocine.fr/film/fichefilm_gen_cfilm=300250.html",
            "306133": "https://www.allocine.fr/film/fichefilm_gen_cfilm=306133.html",
            "228395": "https://www.allocine.fr/film/fichefilm_gen_cfilm=228395.html",
            "275675": "https://www.allocine.fr/film/fichefilm_gen_cfilm=275675.html",
            "299438": "https://www.allocine.fr/film/fichefilm_gen_cfilm=299438.html"
        },
        "2023": {
            "269975": "https://www.allocine.fr/film/fichefilm_gen_cfilm=269975.html",
            "299938": "https://www.allocine.fr/film/fichefilm_gen_cfilm=299938.html",
            "296168": "https://www.allocine.fr/film/fichefilm_gen_cfilm=296168.html",
            "321520": "https://www.allocine.fr/film/fichefilm_gen_cfilm=321520.html",
            "306349": "https://www.allocine.fr/film/fichefilm_gen_cfilm=306349.html",
            "312091": "https://www.allocine.fr/film/fichefilm_gen_cfilm=312091.html",
            "318517": "https://www.allocine.fr/film/fichefilm_gen_cfilm=318517.html",
            "286437": "https://www.allocine.fr/film/fichefilm_gen_cfilm=286437.html",
            "267338": "https://www.allocine.fr/film/fichefilm_gen_cfilm=267338.html",
            "246641": "https://www.allocine.fr/film/fichefilm_gen_cfilm=246641.html"
        },
        "2024":{
            "327723": "https://www.allocine.fr/film/fichefilm_gen_cfilm=327723.html",
            "327724": "https://www.allocine.fr/film/fichefilm_gen_cfilm=327724.html",
            "327721": "https://www.allocine.fr/film/fichefilm_gen_cfilm=327721.html",
            "288404": "https://www.allocine.fr/film/fichefilm_gen_cfilm=288404.html",
            "278742": "https://www.allocine.fr/film/fichefilm_gen_cfilm=278742.html",
            "268384": "https://www.allocine.fr/film/fichefilm_gen_cfilm=268384.html",
            "1000001702": "https://www.allocine.fr/film/fichefilm_gen_cfilm=1000001702.html",
            "302474": "https://www.allocine.fr/film/fichefilm_gen_cfilm=302474.html",
            "274858": "https://www.allocine.fr/film/fichefilm_gen_cfilm=274858.html",
            "313486": "https://www.allocine.fr/film/fichefilm_gen_cfilm=313486.html"
        }       
    }
    for year, film_dict in films.items():
        for film_id, url in film_dict.items():
            print(f" Traitement du film {film_id} ({year})")
            try:
                title = fetch_title(url)
                comments = fetch_reviews(film_id)
                global_id = save_data_csv(csv_path, year, title, comments, global_id)
                print(f"{title} sauvegardé avec {len(comments)} commentaire(s)")
            except Exception as e:
                print(f"Erreur sur {film_id} : {e}")

if __name__ == "__main__":
    main()