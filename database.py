import pandas as pd

class DataBase:
    def exist_database(path):
        # Tentando abrir o banco de dados dimensão USER
        try:
            # Caminho para o banco de dados dimensão
            path_dim = '.\\data\\' + 'dim_user.parquet'
            # Abrindo o arquivo parquet com o Pandas
            # A biblioteca pandas tem uma função que lê arquvios parquet e
            # transforma em Dataframe.
            dim_user = pd.read_parquet(path_dim)
        # Se a abertura do arquivo falhar, retorna falso;
        # ADICIONAR PRINT
        except:
            return False
        # ADICIONAR PRINT
        
        # Tentando abrir o banco de dados FATOS.
        try:
            # Caminho para o banco de dados fact ride.
            path_dim = '.\\data\\' + 'fact_ride.parquet'
            # Abrindo o arquivo parquet com o Pandas
            fact_ride = pd.read_parquet(path_dim)
        # ADICIONAR PRINT
        except:
            return False
        #ADICIONAR PRINT
        
        return True
        
        
    def creat_database(path):
        """
        Criando uma nova tabela na base de dados e salvando no arquivo .parquet.
        Entrada: PATH::string para salvar o arquivo de banco de dados.
        Saída: arquivo .parquet.
        """

        # Criando uma nova tabela de dimensões do usuário
        colums_user = ['id',
                       'name',
                       'email',
                       'phone',
                       'private_key']
        
        df_users = pd.DataFrame(columns=colums_user)

        # Criando a tabela fato de caronas
        columns_ride = ['id',
                        'user_id',
                        'local_origin',
                        'local_destination',
                        'datatime']
        
        df_ride = pd.DataFrame(columns=columns_ride)

        # Salvando os arquivos de banco de dados em .parquet
        # Dimensões do usuário
        save_path_user = path + 'dim_user.parquet'
        df_users.to_parquet(save_path_user)

        # Tabela fato: Carona
        save_path_ride = path + 'fact_ride.parquet'
        df_ride.to_parquet(save_path_ride)

    def ride_search():
        pass