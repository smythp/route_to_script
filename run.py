import os
import subprocess

from flask import Flask, abort
app = Flask(__name__)

@app.route('/')
def index():
    return 'Webhooks'

@app.route('/<script>')
def run(script):

    files = os.listdir()

    if script not in files:
        abort(404)


    rc = subprocess.call(f"./{script}")

    return f'{rc}'

