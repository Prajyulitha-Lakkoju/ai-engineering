import numpy as np

def cosine_similarity(a,b):
    dot_product = np.dot(a,b)
    magnitude_a= np.linalg.norm(a)
    magnitude_b= np.linalg.norm(b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors")
    return dot_product/(magnitude_a*magnitude_b)

vector_a = np.array([1,0])
vector_b = np.array([-1,0])

result = cosine_similarity(vector_a, vector_b)

print("Cosine similarity:", result)