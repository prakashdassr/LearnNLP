# Stop Words in spaCy

This document explains the use of **stop words** in text preprocessing with spaCy. Stop words are common words (e.g., *the*, *and*, *is*) that are usually removed from text to reduce computational complexity without losing significant meaning.

## 1. Common Use Case
One of the primary applications is tagging news articles to identify their topics. For example:

- Input: `Elon Musk is gonna launch rockets.`
- Output Tag: **"SpaceX"** (using the Bag of Words model).

### Bag of Words Model
The Bag of Words (BoW) model represents text as a collection of word counts:

![Bag of Words Example](https://github.com/user-attachments/assets/791da408-d721-4b40-a8f0-26dfab8d0e2b)

## 2. Why Remove Stop Words?
Removing stop words reduces computational overhead by:

- Decreasing the number of tokens to process.
- Retaining only the significant words for analysis.

For example, in the sentence:

- **Original**: `to, and, that, the, you`
- **After Stop Word Removal**: These words are excluded, simplifying the text.

## 3. Exceptions to Stop Word Removal
While stop word removal is helpful, some cases require caution. For example:

- Sentence: *"not a good movie"*
- Removing stop words changes the meaning to: *"good movie"*.

## 4. Using Stop Words in spaCy
### Importing Stop Words
You can access stop words in spaCy as follows:

```python
from spacy.lang.en.stop_words import STOP_WORDS
```

spaCy includes a predefined list of 326 stop words for English.

### Example: Removing Stop Words
The following code demonstrates tokenizing a sentence and removing stop words:

```python
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

sentence = "The new car was launched by Tesla, what an innovation"

# Initialize spaCy pipeline
nlp = spacy.blank("en")
doc = nlp(sentence)

# Tokenize sentence
tokens = [token.text for token in doc]
print("Tokens:", tokens)

# Remove stop words
filtered_tokens = [token for token in tokens if token.lower() not in STOP_WORDS]
print("Filtered Tokens:", filtered_tokens)
```

### Output:
```plaintext
Tokens: ['The', 'new', 'car', 'was', 'launched', 'by', 'Tesla', ',', 'what', 'an', 'innovation']
Filtered Tokens: ['new', 'car', 'launched', 'Tesla', 'innovation']
```

### Accessing the Stop Words List
You can view or modify the list of stop words in spaCy:

```python
# View stop words
print(STOP_WORDS)

# Add a custom stop word
STOP_WORDS.add("innovation")

# Remove a stop word
STOP_WORDS.remove("not")
```

## 5. Relevant Colab Notebook
For an interactive example, refer to the Colab notebook:

[Colab Notebook](https://colab.research.google.com/drive/1BJgAaZTyRkWs4kTNHrGhffUBQeJQ5ZuV?usp=sharing)

---
Using stop words effectively is a crucial step in text preprocessing, enabling efficient and meaningful analysis.

