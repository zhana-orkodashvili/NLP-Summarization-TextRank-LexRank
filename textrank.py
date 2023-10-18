import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import sentences_filter as sf


def preprocess_text(text: str, stops : list[str] = []):
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

def create_similarity_matrix(sentences, words):
    
    # Create an empty similarity matrix
    similarity_matrix = nx.Graph()
    similarity_matrix.add_nodes_from(sentences)
    
    # Calculate the similarity between sentences using cosine similarity
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                sentence1 = sentences[i]
                sentence2 = sentences[j]
                words1 = set(words[i])
                words2 = set(words[j])
                similarity = len(words1.intersection(words2)) / (len(words1) + len(words2))
                similarity_matrix.add_edge(sentence1, sentence2, weight=similarity)
    
    return similarity_matrix


def textrank_summary(text, num_sentences=3, stops: list[str] = []):
    text = sf.remove_sims(text)
    sentences, words = preprocess_text(text, stops)

    dic = {sentences[i]: i for i in range(len(sentences))}
    
    # Create the similarity matrix
    similarity_matrix = create_similarity_matrix(sentences, words)
    
    # Apply the PageRank algorithm to the similarity matrix
    scores = nx.pagerank(similarity_matrix)
    
    # Sort the sentences by their scores
    ranked_sentences = sorted(((scores[sentence], sentence) for sentence in sentences), reverse=True)
    
    # Select the top 'num_sentences' sentences for the summary
    summary_sentences = [sentence for _, sentence in ranked_sentences[:num_sentences]]
    
    summary_sentences = sorted(summary_sentences, key = lambda i: dic[i])
    # Combine the summary sentences into a single string
    summary = ' '.join(summary_sentences)
    
    return summary


