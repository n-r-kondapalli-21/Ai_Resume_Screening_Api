from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_similarity(resume_embedding,jd_embedding):

    score = cosine_similarity([resume_embedding],[jd_embedding])

    return float(score[0][0])


if __name__=="__main__":

    

    resume_embedding = np.load(r"test\embeddings_for_test\resume_embedding.npy")

    jd_embedding = np.load(r"test\embeddings_for_test\resume_embedding.npy")

    r_e = resume_embedding
    j_e = jd_embedding

    score = calculate_similarity(resume_embedding,jd_embedding)

    print(r_e.shape)
    print(j_e.shape)

    print(score)

     