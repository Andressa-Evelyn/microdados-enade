import os
import requests

def download(url):    
    
    try:     
        download_folder = "downloads"        
        filename = os.path.join(download_folder, os.path.basename(url))  
        response = requests.get(url, stream=True, timeout=30) 

        if response.status_code == 200:  #code status
            with open(filename, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024): 
                    f.write(chunk)
            print(f"Download concluído: {filename}")
        else:
            print(f"Erro ao baixar {url} (Status Code: {response.status_code})")

    except requests.exceptions.RequestException as e: 
        print(f" Erro ao baixar {url}: {e}")
        

def download_hrefs(funcao_scrape_hrefs):
    hrefs = funcao_scrape_hrefs
    for href in hrefs:  
        download(href)

