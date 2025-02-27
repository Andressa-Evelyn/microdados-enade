import os

def setup_folders():
    download_folder = "downloads"
    extract_folder = "extracted_files"
    transformed_parquet_files = "transformed_parquet_files"
    os.makedirs(download_folder, exist_ok=True)
    os.makedirs(extract_folder, exist_ok=True)
    os.makedirs(transformed_parquet_files, exist_ok=True)
    return download_folder, extract_folder, transformed_parquet_files

download_folder, extract_folder, transformed_parquet_files = setup_folders()
