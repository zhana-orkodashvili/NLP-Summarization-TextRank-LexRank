# TextRank and LexRank Algorithms for Georgian Language
Simple project to assess and compare text summarization algorithms TextRank and LexRank for Georgian language using Python.

## Table of contents
* [General info](#general-info)
* [Algorithms](#algorithms)

## General info
The purpose of text summarization is to condense a longer piece of text into a shorter version while preserving its main ideas and key information. The two main types of text summarization are extractive summarization and abstractive summarization. 

Extractive summarization involves selecting and extracting important sentences, phrases, or words directly from the original text to form a summary. Abstractive summarization goes beyond extracting sentences from the original text and involves generating new sentences that capture the essence of the source text.

This project uses the most popular algotithms for extractive summarization, TextRank and LexRank.

## Algorithms
   - TextRank: TextRank is a graph-based ranking algorithm inspired by Google's PageRank algorithm. It constructs a graph representation of the text, where sentences are nodes and the edges between them represent the strength of their relationships. The ranking of sentences is determined by iteratively updating their scores based on the votes received from other sentences in the graph.
   - LexRank: LexRank also uses a graph-based approach but focuses on exploiting the concept of eigenvector centrality. It represents the text as a graph, with sentences as nodes, and measures the centrality of sentences based on their cosine similarity to other sentences in the document. The eigenvector centrality of each sentence is computed to determine its importance.
