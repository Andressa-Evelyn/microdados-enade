from scripts.scraping_url_download import scraping_url_download
from scripts.setup_folders import setup_folders
from scripts.download import download_hrefs
from scripts.extract import extrair
from scripts.transformed_parquet_files import transformed_parquet_files
from scripts.reading_parquet import reading_parquet
from scripts.concatenate_dataframe import concatenate_dataframe
from scripts.extract import extraindo_arquivos

def main():

    setup_folders()
    
    download_hrefs(scraping_url_download())
    
    extraindo_arquivos()

    transformed_parquet_files()

    reading_parquet()
    
    concatenate_dataframe()
    
main()