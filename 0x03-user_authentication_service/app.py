#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    response = {"message": "Bienvenue"}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
