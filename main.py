import os
import json
import requests
import numpy as np
import time
from sentence_transformers import SentenceTransformer


# instalar o rust
# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# pip install --upgrade pip

def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Region ": json_region
        })
    }


start_time = time.perf_counter()
model = SentenceTransformer('./model')
end_time = time.perf_counter()
print(end_time - start_time, "seconds")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # model.save('./model')

    sentence_embeddings = model.encode(['o rato roeu a roupa do rei de roma'])

    print(len(sentence_embeddings[0]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
