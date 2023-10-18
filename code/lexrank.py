import nltk
import numpy as np
import networkx as nx
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import sentences_filter as sf

def preprocess_text(text, stops = []):
    # Tokenize the text into sentences and words
    text = text.replace(' ძვ.წ. ', ' ძვწ ').replace(' ძვ. წ. ', ' ძვწ ')\
        .replace(' ე.წ. ', ' ეწ ').replace(' ე. წ. ', ' ეწ ')\
            .replace(' ა.შ. ', ' აშ. ').replace(' ა. შ. ', ' აშ. ')
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    
    # Remove stopwords
    stop_words = set(stops)
    words = [[word for word in sentence if word not in stop_words] for sentence in words]
    
    return sentences, words

def calculate_similarity_matrix(sentences, words):
    num_sentences = len(sentences)
    similarity_matrix = np.zeros((num_sentences, num_sentences))
    
    # Calculate the similarity between sentences using cosine similarity
    for i in range(num_sentences):
        for j in range(num_sentences):
            if i != j:
                sentence1 = words[i]
                sentence2 = words[j]
                similarity = len(set(sentence1).intersection(sentence2)) / (np.log(len(sentence1)) + np.log(len(sentence2)))
                similarity_matrix[i][j] = similarity
    
    return similarity_matrix


def lexrank_summary(text, num_sentences=3, stops = []):
    text = sf.remove_sims(text)
    sentences, words = preprocess_text(text, stops)

    dic = {sentences[i]: i for i in range(len(sentences))}
    
    # Calculate the similarity matrix
    similarity_matrix = calculate_similarity_matrix(sentences, words)
    
    # Convert the similarity matrix to a graph
    similarity_graph = nx.from_numpy_array(similarity_matrix)
    
    # Apply the LexRank algorithm to the similarity graph
    scores = nx.pagerank(similarity_graph)
    
    # Sort the sentences by their scores
    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)
    
    # Select the top 'num_sentences' sentences for the summary
    summary_sentences = [sentence for _, sentence in ranked_sentences[:num_sentences]]
    
    # Combine the summary sentences into a single string
    summary_sentences = sorted(summary_sentences, key = lambda i: dic[i])
    summary = ' '.join(summary_sentences)

    return summary
