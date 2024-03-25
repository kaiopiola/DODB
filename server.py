import os
import json
import fcntl
from flask import Flask
from request_handler import handle_data_request

app = Flask(__name__)

# Route for handling data requests
@app.route('/<database_name>/<table_name>', methods=['POST'])
def handle_request(database_name, table_name):
    return handle_data_request(database_name, table_name)

if __name__ == "__main__":
    app.run(debug=True)
