# 🛫 Pipeline de Dados com Apache Airflow

Este repositório contém o projeto desenvolvido durante o curso da Alura.

## 📌 Descrição do Projeto

Neste projeto, foi criado um pipeline de dados para uma empresa de turismo, com o objetivo de obter semanalmente dados da previsão do tempo. O fluxo é executado **automaticamente toda segunda-feira**, orquestrado por uma DAG no Apache Airflow.

Os dados são coletados por meio de uma API, tratados com Python e armazenados em pastas organizadas por semana. Este processo permite à empresa planejar melhor seus serviços com base nas condições climáticas previstas.

## ⚙️ Tecnologias e Ferramentas Utilizadas

- **Apache Airflow**: ferramenta de orquestração de workflows
- **Python**: para manipulação dos dados
- **Pandas**: para leitura e tratamento de arquivos CSV
- **BashOperator & PythonOperator**: para criação das tasks
- **Visual Crossing API**: para acesso às informações climáticas

## 🚀 O que foi aprendido

Durante o curso, foram abordados os seguintes tópicos:

- Conceitos fundamentais do Apache Airflow: DAGs, Tasks, Operators
- Estrutura e componentes da arquitetura do Airflow
- Instalação e configuração do Airflow em ambiente local
- Criação de DAGs agendadas com `schedule_interval`
- Uso do BashOperator para criação de diretórios
- Uso do PythonOperator para execução de funções de extração e salvamento de dados
- Organização e modularização de um pipeline de dados automatizado



