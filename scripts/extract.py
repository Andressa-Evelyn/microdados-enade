import os
import zipfile
import rarfile
import py7zr
import magic

download_folder = "downloads"
extract_folder = "extracted_files"


def file_type(filename):
    tipo = magic.Magic(mime=True).from_file(filename)

    if "zip" in tipo:
        return "zip"
    elif "rar" in tipo:
        return "rar"
    elif "7z" in tipo or "x-7z-compressed" in tipo:
        return "7z"
    else:
        return None


def extrair(filename, extract_folder):


    if not os.path.exists(filename):
        raise FileNotFoundError(f"Arquivo {filename} não encontrado.")
    
    formato_real = file_type(filename)
    
    if formato_real == "zip":
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(extract_folder)
    
    elif formato_real == "rar":
        with rarfile.RarFile(filename) as rar_ref:
            rar_ref.extractall(extract_folder)
    
    elif formato_real == "7z":
        with py7zr.SevenZipFile(filename, "r") as sevenz_ref:
            sevenz_ref.extractall(extract_folder)

def extraindo_arquivos():
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        extrair(file_path, extract_folder)