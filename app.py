import flask
import json
import numpy as np
from flask import jsonify
from flask import Flask, request
from sentence_transformers import SentenceTransformer

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def decode(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        # 👇️ alternatively use str()
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()


model = SentenceTransformer('./model')


def normalize(embedding):
    items = []
    for item in embedding:
        items.append(decode(item))

    return items


@app.route('/sentence-embedding', methods=['POST'])
def home():
    request_data = request.get_json()

    sentence = request_data['sentence']
    sentence_embeddings = model.encode([sentence])

    return jsonify({
        "statusCode": 200,
        "embedding": normalize(sentence_embeddings[0])
    })


app.run()
