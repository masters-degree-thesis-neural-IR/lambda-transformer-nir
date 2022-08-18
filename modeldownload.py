from sentence_transformers import SentenceTransformer

model = SentenceTransformer('neuralmind/bert-base-portuguese-cased')
model.save('./model')