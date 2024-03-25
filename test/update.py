import requests
import json

base_url = 'http://127.0.0.1:5000'
database_name = 'my_db'
table_name = 'users'

# Definindo os filtros para atualizar registros com idade maior que 50
filters = [
    {"key": "age", "operator": ">", "value": 50}
]

# Definindo os novos dados para atualizar os registros correspondentes
new_data = {
    "age": 60
}

# Montando o payload da solicitação
request_data = {
    "operation": "UPDATE",
    "filters": filters,
    "updated_record": new_data
}

# Enviando a solicitação UPDATE para atualizar registros com base nos filtros
response = requests.post(f"{base_url}/{database_name}/{table_name}", json=request_data)

# Exibindo a resposta
print(response.json())
