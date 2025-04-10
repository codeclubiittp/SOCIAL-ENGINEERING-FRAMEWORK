from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='logs/webhooks.log', level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def receive():
    data = request.get_json()
    logging.info(f"Received webhook: {data}")
    return 'OK', 200
