from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json') as f:
        d = json.load(f)
    return d

@app.route('/confirmed')
def index():
    with open('data.json') as f:
        d = json.load(f)
    return d['confirmed']

@app.route('/deaths')
def index():
    with open('data.json') as f:
        d = json.load(f)
    return d['deaths']

@app.route('/recovered')
def index():
    with open('data.json') as f:
        d = json.load(f)
    return d['recovered']

@app.route('/latest')
def index():
    with open('data.json') as f:
        d = json.load(f)
    return d['latest']

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)