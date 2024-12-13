# Introduction to N-Grams

## Bag of Words (BoW)
Bag of Words is a technique in natural language processing (NLP) that represents text as a collection of individual words and their counts, ignoring grammar and word order. It is commonly used for text classification and information retrieval tasks.

### Illustration of Bag of Words
![Bag of Words Example 1](https://github.com/user-attachments/assets/530684cc-3439-4da7-b9fa-9a0ec064ee01)

![Bag of Words Example 2](https://github.com/user-attachments/assets/19b41349-a166-4171-9d25-1592f9ca52fc)

### Limitation of Bag of Words
While effective in capturing word frequency, the Bag of Words approach loses the context and meaning conveyed by the order of words. For example, the sentences:

- "The dog bit the man."
- "The man bit the dog."

Both would have the same representation in a Bag of Words model, even though their meanings are different.

## N-Grams
N-Grams provide a solution to this limitation by capturing the sequence of words in a text. An N-Gram is a contiguous sequence of **N** items (words or characters) from a given text. By considering the context of neighboring words, N-Grams help preserve some of the word order and improve the semantic understanding of text.

### Types of N-Grams
1. **Unigrams (1-Gram)**: Single words (e.g., "The", "dog", "barked")
2. **Bigrams (2-Gram)**: Pairs of consecutive words (e.g., "The dog", "dog barked")
3. **Trigrams (3-Gram)**: Triplets of consecutive words (e.g., "The dog barked")
4. **N-Grams (N > 3)**: Higher-order combinations of N words.

### Example:
For the sentence: "The quick brown fox jumps over the lazy dog."

- **Unigrams**: ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
- **Bigrams**: ["The quick", "quick brown", "brown fox", "fox jumps", "jumps over", "over the", "the lazy", "lazy dog"]
- **Trigrams**: ["The quick brown", "quick brown fox", "brown fox jumps", "fox jumps over", "jumps over the", "over the lazy", "the lazy dog"]

### Sliding Window Mechanism
To generate N-Grams, a sliding window approach is used:
- Start at the beginning of the sentence.
- Move the window one word at a time.
- Extract the sequence of N words within the window.

This technique ensures that all possible combinations of N consecutive words are captured.

## Applications of N-Grams
1. **Text Classification**: Capturing contextual information for sentiment analysis, spam detection, etc.
2. **Language Modeling**: Predicting the next word based on the preceding words.
3. **Information Retrieval**: Improving search engine accuracy by matching phrases instead of single words.
4. **Speech Recognition**: Enhancing understanding by considering word combinations.

---

This document provides an introduction to N-Grams and their importance in overcoming the limitations of the Bag of Words model. By leveraging N-Grams, NLP tasks can achieve better performance through improved context awareness.

