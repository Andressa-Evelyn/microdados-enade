from scripts.scraping_url_download import scraping_url_download
from scripts.setup_folders import setup_folders
from scripts.download import download_hrefs
from scripts.extract import extrair
from scripts.transformed_parquet_files import transformed_parquet_files
from scripts.reading_parquet import reading_parquet
from scripts.concatenate_dataframe import concatenate_dataframe

def main():
    setup_folders()
    
    urls = scraping_url_download()

    download_hrefs(urls)
    
    extrair()
    
    transformed_parquet_files()

    reading_parquet()
    
    concatenate_dataframe()
    
    