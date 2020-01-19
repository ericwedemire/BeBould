#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello, fuckers!"

if __name__ == "__main__":
    app.run()