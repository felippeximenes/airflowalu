from airflow import DAG
import pendulum
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.python_operator import PythonOperator # Utilizado para executar codigos e funções python
from airflow.macros import ds_add # Para somar as datas
import os # Utilizada para manipulação de arquivos e diretórios
from os.path import join # Juntar paths
import pandas as pd # Biblioteca para manipulação de dados

with DAG(
        "dados_climaticos",
        start_date=pendulum.datetime(2025, 5, 5, tz="UTC"),
        schedule_interval='0 0 * * 1', # executar toda segunda feira # executar toda segunda feira # O primeiro 0 é a hora e o segundo 0 é o minuto # O * para rodar o mes todo
) as dag:

    tarefa_1 = BashOperator( # Esse parâmetro existe em todos os operadores do Airflow. Ele é utilizado para definir o nome da tarefa que estamos instanciando.
            task_id = 'cria_pasta',
            bash_command = 'mkdir -p "/home/Felippe/Documents/airflowalu/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
            )
    
    def extrai_dados(data_interval_end): # O conteudo dessa funcao sera basicamente o conteudo de dados desenvolvido para a empressa
        city = 'Boston'
        key = 'GYDHYHQDYQ2NVNL4EWCFH4BPD'

        # O join fuizado para juntar o URL base da API com os parâmetros necessários para a requisição
        # Aqui a URL é construída com os parâmetros necessários para a requisição da API
        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                    f'{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

        dados = pd.read_csv(URL) # Lê os dados da URL e armazena em um DataFrame do pandas
        # Aqui os dados são lidos a partir da URL e armazenados em um DataFrame do pandas       
        

        # Definindo o caminho
        file_path = f'/root/airflowalu/seamana={data_interval_end}'
        
        # Criando o csv com o pandas
        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv') # Info mais importantes 
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')# Info mais importantes 
    
    tarefa_2 = PythonOperator(
            task_id = 'extrai_dados',
            python_callable = extrai_dados, # Passa o nome da função ou codigo python que deseja executar
            op_kwargs= {'data_interval_end' : '{{data_interval_end.strftime("%Y-%m-%d")}}'} # Dicionaerio de argumentos que deseja passar para a função pythoncallable #Isso mesmo! Esse parâmetro é utilizado para definir os argumentos que estamos utilizando na função que o PythonOperator vai executar. Nós passamos essa informação no formato de um dicionário de argumentos de palavras-chave que serão descompactados na função.
        )

    tarefa_1 >> tarefa_2
    
