import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    # Obtenir le contenu HTML de la page
    response = requests.get(url)
    html_content = response.content

    # Utiliser BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Trouver tous les éléments <a> (liens) dans le HTML
    links = soup.find_all('a')

    # Extraire les URLs des liens
    all_links = [link.get('href') for link in links]

    return all_links

# Remplacez 'https://example.com' par l'URL du site que vous souhaitez scraper
site_url = 'https://lenouvelliste.com'
all_links = get_all_links(site_url)

# Afficher les liens
for link in all_links:
    print(link)
