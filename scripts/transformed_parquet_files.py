import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def transformed_parquet_files():
    root_dir = "/home/951551482@adm.unifor.br/Documentos/microdados-enade/extracted_files"
    base_destination = "/home/951551482@adm.unifor.br/Documentos/microdados-enade/transformed_parquet_files"

    for year in range(2013, 2022):

        possible_folders = [
            os.path.join(root_dir, f"microdados_Enade_{year}_LGPD", "2.DADOS"),
            os.path.join(root_dir, f"microdados_Enade_{year}_LGPD", "2. DADOS")
        ]

        folder_path = next((folder for folder in possible_folders if os.path.exists(folder)), None)
        if folder_path:
            destination_folder = os.path.join(base_destination, f"microdados_Enade_{year}_LGPD")
            os.makedirs(destination_folder, exist_ok=True)
            
            for file in os.listdir(folder_path):
                if file.startswith(f"microdados{year}_arq") and file.endswith(".txt"):
                    source_file = os.path.join(folder_path, file) #arquivo
                    
                    parquet_file = os.path.join(destination_folder, f"{os.path.splitext(file)[0]}.parquet") #nome do arquivo parquet

                    #df
                    try:
                        df = pd.read_csv(source_file, delimiter=';', dtype=str , low_memory=False)
                    except Exception as e:
                        print(f"Erro ao ler o arquivo {source_file}: {e}")
                        continue

                    table = pa.Table.from_pandas(df)

                    try:
                        pq.write_table(table, parquet_file)
                        print(f'Arquivo Parquet criado: {parquet_file}')
                    except Exception as e:
                        print(f"Erro ao escrever o arquivo Parquet {parquet_file}: {e}")
                        continue
                
            