from flask import Flask, render_template
import webInterface as web
import time
import sys

app = Flask(__name__)
count = 1

@app.route('/')
def index():
    global count
    if count > 30:
        text = "Out of headlines. Restarting..."
        count = 0
    else:
        text = web.getHeadlines(count)
    timeout = web.getTimeout()
    web.speech(text, count)
    count += 1
    return render_template('index.html', marquee=text, timeout=timeout)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
