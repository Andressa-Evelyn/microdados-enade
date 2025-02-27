from bs4 import BeautifulSoup
import requests

def scraping_url_download() -> list:
    url = 'https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    content_core = soup.find(id="content-core")
    links = content_core.find_all("a")
    hrefs = [link.get("href") for link in links if link.get("href")]

    return hrefs
