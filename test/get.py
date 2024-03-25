import json
import requests

# Função para realizar uma solicitação GET com filtros
def get_data_with_filters(base_url, database_name, table_name, filters):
    response = requests.post(f"{base_url}/{database_name}/{table_name}", json=filters)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.text}")
        return None

if __name__ == "__main__":
    base_url = 'http://127.0.0.1:5000'
    database_name = 'my_db'
    table_name = 'users'
    filters = {
        "operation": "GET",
        "filters": [
            {"key": "age", "operator": ">", "value": 80},
            {"key": "cash", "operator": ">=", "value": 7000}
        ]
    }
    print(filters)
    filtered_data = get_data_with_filters(base_url, database_name, table_name, filters)
    if filtered_data:
        print("Filtered data:")
        print(json.dumps(filtered_data, indent=4))
