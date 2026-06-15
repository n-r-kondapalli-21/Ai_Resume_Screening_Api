from sentence_transformers import SentenceTransformer

model = SentenceTransformer("./Ai_models/all-MiniLM-L6-v2")


def generate_embedding(text):

    embedding = model.encode(text)

    return embedding



if __name__=="__main__":

    text="hello to all"

    embedding = generate_embedding(text)

    print(type(embedding))
    print(embedding.shape)




