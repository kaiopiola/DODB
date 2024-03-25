# functions/delete.py
import os
import json
from functions.filters import apply_filters
from functions import locking

# Function to delete records from the table based on filters
def delete_records_from_table(database_name, table_name, dbt_file, filters=None):
    if os.path.exists(dbt_file):
        with open(dbt_file, 'r+') as file:
            locking.lock_file(file)  # Get a file locked before writing
            data = json.load(file)
            table_data = data.get('data', [])
            
            # Apply filters if provided
            if filters:
                table_data = apply_filters(table_data, filters)
            
            # Remove records that match the filter criteria
            removed_records = []
            for record in table_data:
                table_data.remove(record)
                removed_records.append(record)
            
            # Update the data in the file
            data['data'] = table_data
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            
            locking.unlock_file(file)  # Unlock file after writing
        return {"message": f"{len(removed_records)} record(s) deleted successfully"}, 200
    else:
        return {"message": f"Table '{table_name}' in database '{database_name}' not found"}, 404
