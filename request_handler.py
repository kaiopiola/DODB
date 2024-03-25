import os
import json
import fcntl
from flask import jsonify, request
from functions import create, get, update, delete

# Função para manipular solicitações de dados
def handle_data_request(database_name, table_name):
    dbt_file = f'./db/{database_name}/{table_name}.dbt'
    request_data = request.json
    
    if 'operation' not in request_data:
        return jsonify({"message": "Operation not specified"}), 400
    
    operation = request_data['operation']
    
    if operation == 'GET':
        return get.get_table_records(database_name, table_name, dbt_file, request_data)
    elif operation == 'CREATE':
        return create.add_record_to_table(database_name, table_name, dbt_file, request_data)
    elif operation == 'UPDATE':
        return update.update_record_in_table(database_name, table_name, dbt_file, request_data)
    elif operation == 'DELETE':
        return delete.delete_records_from_table(database_name, table_name, dbt_file, request_data)
    else:
        return jsonify({"message": f"Unsupported operation: {operation}"}), 400
