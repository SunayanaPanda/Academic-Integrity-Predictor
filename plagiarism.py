import nltk
import torch
from sentence_transformers import util
from model import model

# Download tokenizer (runs only once)
nltk.download("punkt", quiet=True)


def highlight_similar_text(source_text, compare_text, similarity_threshold=0.70):
    """
    Compare two texts sentence by sentence and return
    highlighted similar sentences.
    """

    try:
        # Split into sentences
        source_sentences = nltk.sent_tokenize(source_text)
        compare_sentences = nltk.sent_tokenize(compare_text)

        if not source_sentences or not compare_sentences:
            return source_text, compare_text, []

        # Generate sentence embeddings
        source_embeddings = model.encode(
            source_sentences,
            convert_to_tensor=True
        )

        compare_embeddings = model.encode(
            compare_sentences,
            convert_to_tensor=True
        )

        highlighted_source = source_text
        highlighted_compare = compare_text

        similar_segments = []

        # Compare every source sentence
        for i, source_sentence in enumerate(source_sentences):

            similarities = util.cos_sim(
                source_embeddings[i],
                compare_embeddings
            )

            max_similarity, max_index = torch.max(
                similarities,
                dim=1
            )

            similarity_score = max_similarity.item()
            matched_sentence = compare_sentences[max_index.item()]

            if similarity_score >= similarity_threshold:

                similar_segments.append(
                    {
                        "source_sentence": source_sentence,
                        "compare_sentence": matched_sentence,
                        "similarity": round(similarity_score, 4),
                    }
                )

                highlighted_source = highlighted_source.replace(
                    source_sentence,
                    f"<mark>{source_sentence}</mark>"
                )

                highlighted_compare = highlighted_compare.replace(
                    matched_sentence,
                    f"<mark>{matched_sentence}</mark>"
                )

        return (
            highlighted_source,
            highlighted_compare,
            similar_segments,
        )

    except Exception as e:
        print(e)
        return source_text, compare_text, []