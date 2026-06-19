from flask import Flask, request, jsonify
import requests
import base64
import os

app = Flask(__name__)

ALEGRA_EMAIL = "ventas@dvtdistribuidora.com"
ALEGRA_TOKEN = "c2cbdf72f4b54fe83ff6"
credentials = base64.b64encode(f"{ALEGRA_EMAIL}:{ALEGRA_TOKEN}".encode()).decode()

@app.route('/factura', methods=['POST'])
def crear_factura():
    data = request.json
    headers = {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://app.alegra.com/api/v1/invoices",
        json=data,
        headers=headers
    )
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
