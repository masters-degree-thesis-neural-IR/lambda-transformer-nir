# import os
# import json
# import requests
# import numpy as np
# import time

from sentence_transformers import SentenceTransformer

# instalar o rust
# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# pip install --upgrade pip

model = SentenceTransformer('./model')


def lambda_handler(event, context):
    # json_region = os.environ['AWS_REGION']

    # sentence = event.get("sentence")
    # sentence_embeddings = model.encode([sentence])
    # json.dumps(str(sentence_embeddings[0]))

    return {
        "statusCode": 200,
        "embedding": "Olá mundo"
    }


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     # model.save('./model')
#
#     sentence_embeddings = model.encode(['o rato roeu a roupa do rei de roma'])
#     print(json.dumps(str(sentence_embeddings[0])))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
