from flask import Flask, render_template
import os

app = Flask(__name__)

def read_log(log_file):
    if not os.path.exists(log_file):
        return ["No log data found."]
    with open(log_file, 'r') as f:
        return f.readlines()

@app.route('/')
def dashboard():
    credentials = read_log('logs/harvested_credentials.log')
    return render_template('index.html', creds=credentials)

def run_dashboard():
    print("[+] Launching dashboard at http://localhost:5000")
    app.run(port=5000)
