import json
import numpy as np
from sentence_transformers import SentenceTransformer


# instalar o rust
# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            # 👇️ alternatively use str()
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


model = SentenceTransformer('./model')


def lambda_handler(event, context):
    # json_region = os.environ['AWS_REGION']

    sentence = event.get("sentence")
    sentence_embeddings = model.encode([sentence])

    return json.dumps(
        {
            "statusCode": 200,
            "embedding": sentence_embeddings[0]
        },
        cls=NpEncoder
    )


def response(message, status_code):
    return {
        'statusCode': status_code,
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     # model.save('./model')
#
#     sentence_embeddings = model.encode(['o rato roeu a roupa do rei de roma'])
#     print(json.dumps(str(sentence_embeddings[0])))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
