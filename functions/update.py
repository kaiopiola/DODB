# functions/update.py
import os
import json
from .filters import apply_filters, apply_single_filter
from functions import locking

# Function to update a record in the table
def update_record_in_table(database_name, table_name, dbt_file, request_data):
    if os.path.exists(dbt_file):
        updated_record_data = request_data.get('updated_record')
        if updated_record_data:
            with open(dbt_file, 'r+') as file:
                locking.lock_file(file)  # Get a file locked before writing
                data = json.load(file)
                
                # Apply filters if provided
                if 'filters' in request_data:
                    filtered_data = apply_filters(data['data'], request_data['filters'])
                else:
                    filtered_data = data['data']
                
                # Find the record in the table and update its data
                for record in filtered_data:
                    if all(apply_single_filter(record, key, operator, value) for key, operator, value in updated_record_data.items()):
                        record.update(updated_record_data)
                        break
                
                # Write the updated data to the file
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                
                locking.unlock_file(file)  # Unlock file after writing
