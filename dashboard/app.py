from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        'methane': random.randint(200, 600),
        'temperature': random.randint(25, 35),
        'humidity': random.randint(50, 80),
        'status': 'Normal'
    }

    if data['methane'] > 500:
        data['status'] = 'Critical'

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)