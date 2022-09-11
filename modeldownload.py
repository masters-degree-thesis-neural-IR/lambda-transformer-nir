from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('neuralmind/bert-base-portuguese-cased')
model = SentenceTransformer('all-MiniLM-L6-v2')
model.save('./model')