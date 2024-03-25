import json
import random
import time
import requests

# Função para gerar um registro de usuário aleatório
def generate_random_user():
    return {
        "id": random.randint(1, 1000000),
        "name": "User" + str(random.randint(1, 1000000)),
        "age": random.randint(18, 100)
    }

# Função para enviar solicitações POST para inserir dados na tabela via API
def insert_data_through_api(base_url, database_name, table_name, num_records):
    start_time = time.time()
    for _ in range(num_records):
        user_data = generate_random_user()
        response = requests.post(f"{base_url}/{database_name}/{table_name}", json=user_data)
        if response.status_code != 201:
            print(f"Error: {response.text}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

if __name__ == "__main__":
    base_url = 'http://127.0.0.1:5000'
    database_name = 'my_db'
    table_name = 'users'
    num_records = 10000  # Defina o número de registros que deseja inserir
    elapsed_time = insert_data_through_api(base_url, database_name, table_name, num_records)
    print(f"Time elapsed for inserting {num_records} data via API: {elapsed_time} seconds")
