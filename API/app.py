from flask import Flask, jsonify
from flask_cors import CORS
from config.db import prendas_collection

app = Flask(__name__)
CORS(app)

@app.route('/api/prendas', methods=['GET'])
def obtener_prendas():
    try:
        prendas = list(prendas_collection.find({}, {'_id': 0}))
        return jsonify(prendas)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)