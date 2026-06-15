from sentence_transformers import SentenceTransformer

model = SentenceTransformer("./Ai_models/all-MiniLM-L6-v2")


def generate_embedding(text):

    embedding = model.encode(text)

    return embedding


if __name__=="__main__":
    text = "hello to all"

    emb=generate_embedding(text)

    print(len(emb))