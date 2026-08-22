from sentence_transformers import SentenceTransformer, util

# Load the pretrained Sentence Transformer model only once
model = SentenceTransformer("all-mpnet-base-v2")


def generate_embedding(text):
    """
    Convert text into a semantic embedding.
    """
    return model.encode(text, convert_to_tensor=True)


def calculate_similarity(text1, text2):
    """
    Calculate semantic similarity between two texts.
    Returns similarity score (0 to 1).
    """
    emb1 = generate_embedding(text1)
    emb2 = generate_embedding(text2)

    score = util.cos_sim(emb1, emb2).item()
    return score