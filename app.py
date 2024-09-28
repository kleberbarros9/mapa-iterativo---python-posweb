from flask import Flask, jsonify, send_from_directory
from data import carregar_dados

app = Flask(__name__)

# Rota para fornecer os dados em formato JSON
@app.route('/api/data')
def api_data():
    data = carregar_dados()
    return jsonify(data)

# Rota para servir o front-end (HTML, CSS, JS)
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    app.run(debug=True)
