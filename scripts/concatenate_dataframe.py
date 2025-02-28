import os
import pandas as pd


def concatenate_dataframe():
    base_dir = "/home/951551482@adm.unifor.br/Documentos/microdados-enade/transformed_parquet_files"
    dataframes = {}

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".parquet"):
                sufixo = file.split('_')[-1].split('.')[0] 
                file_path = os.path.join(root, file)
                df = pd.read_parquet(file_path)
                
                # serve para não sobrescrever
                if sufixo in dataframes:
                    dataframes[sufixo] = pd.concat([dataframes[sufixo], df], ignore_index=True)
                else:
                    dataframes[sufixo] = df

#  dataframes['arqx'] contém todos os DataFrames concatenados com sufixo 'arqx'

concatenate_dataframe()