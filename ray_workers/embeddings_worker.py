import ray
import numpy as np

@ray.remote
def embed_text(batch):
    # placeholder: return random vectors
    return [np.random.rand(768).tolist() for _ in batch]

if __name__ == "__main__":
    ray.init()
    vecs = ray.get(embed_text.remote(["hello","world"]))
    print(len(vecs), "embeddings generated")
