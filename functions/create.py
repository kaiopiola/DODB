# functions/create.py
import os
import json
import fcntl
from functions import locking

# Function to handle POST operation
def add_record_to_table(database_name, table_name, dbt_file, request_data):
    if os.path.exists(dbt_file):
        new_record_data = request_data.get('new_record')
        if new_record_data:
            with open(dbt_file, 'r+') as file:
                locking.lock_file(file)  # Get a file locked before writing
                data = json.load(file)
                data['data'].append(new_record_data)
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                locking.unlock_file(file)  # Unlock file after writing
            return {"message": f"Record added to '{table_name}' in database '{database_name}' successfully"}, 201
        else:
            return {"message": "New record data not provided"}, 400
    else:
        return {"message": f"Table '{table_name}' in database '{database_name}' not found"}, 404
