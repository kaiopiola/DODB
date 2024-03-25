import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota para listar todos os registros de uma tabela em um banco de dados
@app.route('/<database_name>/<table_name>', methods=['GET'])
def get_table_records(database_name, table_name):
    dbt_file = f'./db/{database_name}/{table_name}.dbt'
    if os.path.exists(dbt_file):
        with open(dbt_file, 'r') as file:
            table_data = json.load(file)
        return jsonify(table_data)
    else:
        return jsonify({"message": f"Table '{table_name}' in database '{database_name}' not found"}), 404

# Rota para adicionar um novo registro a uma tabela em um banco de dados
@app.route('/<database_name>/<table_name>', methods=['POST'])
def add_record_to_table(database_name, table_name):
    dbt_file = f'./db/{database_name}/{table_name}.dbt'
    new_record_data = request.json
    if os.path.exists(dbt_file):
        # Ler os dados existentes no arquivo
        with open(dbt_file, 'r') as file:
            data = json.load(file)
        # Adicionar o novo registro aos dados existentes
        data['data'].append(new_record_data)
        # Escrever os dados atualizados de volta para o arquivo
        with open(dbt_file, 'w') as file:
            json.dump(data, file, indent=4)
        return jsonify({"message": f"Record added to '{table_name}' in database '{database_name}' successfully"}), 201
    else:
        return jsonify({"message": f"Table '{table_name}' in database '{database_name}' not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
