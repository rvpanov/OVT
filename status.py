from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

STATUS_FILE = 'status.txt'
LOG_FILE = 'status_log.txt'

def get_status():
 
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip().lower()
    return 'off'

def set_status(status):
   
    status = status.lower()
    

    with open(STATUS_FILE, 'w', encoding='utf-8') as f:
        f.write(status)
  
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} - {status}\n")

@app.route('/')
def index():
    return "Доступные команды:\n/on\n/off\n/status\n/api/status"

@app.route('/on')
def turn_on():
    set_status('on')
    return "OK: Статус изменен на ON"

@app.route('/off')
def turn_off():
    set_status('off')
    return "OK: Статус изменен на OFF"

@app.route('/status')
def status_page():
   
    current = get_status().upper()
    return f"<h1>Status: {current}</h1>"

@app.route('/api/status')
def api_status():
    
    return get_status()

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000)
