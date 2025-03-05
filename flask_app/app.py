from flask import Flask, jsonify
import requests

app = Flask(__name__)

DJANGO_API_URL = "http://django:8000/api/products/"  # Django service in Docker

@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get(DJANGO_API_URL)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run()

# Note: if __name__ == "__main__" block is ignored because Gunicorn will manage the application.
