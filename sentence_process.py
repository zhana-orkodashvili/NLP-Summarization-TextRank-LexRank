import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from stops import stops_new
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein


def calculate_similarity(sentence1, sentence2):
    # Tokenize the sentences
    tokens1 = word_tokenize(sentence1)
    tokens2 = word_tokenize(sentence2)
    
    # Remove stopwords
    stop_words = set(stops_new)
    filtered_tokens1 = [token for token in tokens1 if token not in stop_words and len(token) > 2]
    filtered_tokens2 = [token for token in tokens2 if token not in stop_words and len(token) > 2]
    

    tok1 = filtered_tokens1.copy()
    tok2 = filtered_tokens2.copy()
    if not len(tok1) or not len(tok2):
        return 0 
    for i in filtered_tokens1:
        if i not in tok1:
            continue
        for j in filtered_tokens2:
            if j not in tok2:
                continue
            if Levenshtein.distance(i, j) <= 2:
                tok1.remove(i)
                tok2.remove(j)
                break
    first_end_product_left = len(tok1) / len(filtered_tokens1)
    second_end_product_left = len(tok2) / len(filtered_tokens2)
    avg_end_product_left = first_end_product_left + second_end_product_left
    avg_end_product_left /= 2
    similarity_coefficient = 1 - avg_end_product_left
    return similarity_coefficient

