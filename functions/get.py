# functions/get.py
import os
import json
from flask import jsonify
from functions import filters
from functions import locking

# Function to handle GET operation
def get_table_records(database_name, table_name, dbt_file, request_data):
    if os.path.exists(dbt_file):
        with open(dbt_file, 'r') as file:
            locking.lock_file(file)  # Get a file locked before reading
            table_data = json.load(file)
            locking.unlock_file(file)  # Unlock file after reading
        
        if 'filters' in request_data:
            filtered_data = filters.apply_filters(table_data['data'], request_data['filters'])
            return jsonify(filtered_data)
        else:
            return jsonify(table_data['data'])
    else:
        return jsonify({"message": f"Table '{table_name}' in database '{database_name}' not found"}), 404
