import os
import pandas as pd

def reading_parquet():
    base_dir = "/home/951551482@adm.unifor.br/Documentos/microdados-enade/transformed_parquet_files"
    dataframes = {}

    for root, dirs, files in os.walk(base_dir): 
        for file in files:
            if file.endswith(".parquet"):
                sufixo = file.split('_')[-1].split('.')[0] #arq1 ....arq43
                file_path = os.path.join(root, file)
                df = pd.read_parquet(file_path)
