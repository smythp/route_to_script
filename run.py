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

    script_path = './run'

    result = subprocess.run(script_path, env=os.environ, stdout=subprocess.PIPE)
    out = result.stdout.decode().strip()

    # rc = subprocess.call(f"./{script}")
    out = out.replace('\n',  '<br>')

    return f'{out}'



if __name__ == "__main__":
    app.run(host='0.0.0.0')
