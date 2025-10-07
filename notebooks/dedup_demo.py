from datasketch import MinHash, MinHashLSH
from simhash import Simhash

def shingles(s, k=5):
    tokens = s.lower().split()
    return [" ".join(tokens[i:i+k]) for i in range(max(1,len(tokens)-k+1))]

def minhash(sig):
    m = MinHash(num_perm=64)
    for token in sig:
        m.update(token.encode('utf8'))
    return m

docs = {
    "a": "Large language models are trained on diverse text data from the web.",
    "b": "Language models are trained on diverse text from across the web.",
    "c": "Completely unrelated sentence about cooking pasta with tomato sauce."
}

# MinHash LSH
lsh = MinHashLSH(threshold=0.7, num_perm=64)
mh = {}
for k, v in docs.items():
    mh[k] = minhash(shingles(v, k=5))
    lsh.insert(k, mh[k])

print("Candidates near 'a':", lsh.query(mh["a"]))

# SimHash
for k, v in docs.items():
    print(k, Simhash(v).value)
