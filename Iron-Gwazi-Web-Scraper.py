"""
Web Scraping - Mi primer scraper
Extrae información de la página de Wikipedia de Iron Gwazi
Basado en el libro "Web Scraping with Python" de Ryan Mitchell
"""

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def get_wikipedia_page(url):
    """Obtiene y parsea una página de Wikipedia con un User-Agent real"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
    }
    req = Request(url, headers=headers)
    html = urlopen(req)
    return BeautifulSoup(html.read(), 'html.parser')

def extract_info(bs):
    """Extrae información relevante de la página"""
    titulo = bs.find('h1', class_='firstHeading').text
    
    # El primer <p> es mw-empty-elt (vacío), el segundo tiene el resumen real
    parrafos = bs.find_all('p')
    if len(parrafos) > 1:
        primer_parrafo = parrafos[1].text.strip()
    else:
        primer_parrafo = "No se encontró el párrafo de resumen"
    
    return {
        'titulo': titulo,
        'primer_parrafo': primer_parrafo[:500] + '...' if len(primer_parrafo) > 500 else primer_parrafo
    }

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Iron_Gwazi'
    bs = get_wikipedia_page(url)
    info = extract_info(bs)
    
    print(f"Título: {info['titulo']}")
    print(f"Resumen: {info['primer_parrafo']}")