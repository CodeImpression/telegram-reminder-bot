from flask import Flask
from threading import Thread
from reminder import send_reminder 

app = Flask('')

@app.route('/')
def home():
    send_reminder()
    return "Bot is alive and sent a message!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()