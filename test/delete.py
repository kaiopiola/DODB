import requests
import json

base_url = 'http://127.0.0.1:5000'
database_name = 'my_db'
table_name = 'users'

# Definindo os filtros para excluir registros com idade menor que 30
filters = [
    {"key": "age", "operator": "<", "value": 30}
]

# Montando o payload da solicitação
request_data = {
    "operation": "DELETE",
    "filters": filters
}

# Enviando a solicitação DELETE para excluir registros com base nos filtros
response = requests.post(f"{base_url}/{database_name}/{table_name}", json=request_data)

# Exibindo a resposta
print(response.json())
