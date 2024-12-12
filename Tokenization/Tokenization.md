# Tokenization with spaCy

This guide introduces **tokenization** in Natural Language Processing (NLP) using spaCy. Tokenization is the process of breaking down text into smaller components like words, phrases, or symbols.

## 1. Setting Up
To begin, import the spaCy library:

```python
import spacy as sp
```

### Creating an NLP Component
To create a blank NLP pipeline for the English language:

```python
nlp = sp.blank("en")
```

- The `nlp` object is initialized for English (`en`).
- The return type of `nlp` is:
  
  ```
  <spacy.lang.en.English object at 0x...>
  ```

### Tokenizing a Sentence
Use the `nlp` object to tokenize an English sentence:

```python
sentence = nlp("Hello, I am Prakash Dass R")
for word in sentence:
    print(word)
```

Each `word` represents a token in the input text.

## 2. How Tokenization Works in spaCy
The tokenization process in spaCy follows this sequence:

- **Prefixes**: Identifies leading characters (e.g., `$`, `(`).
- **Suffixes**: Identifies trailing characters (e.g., `.`, `)`).
- **Exceptions**: Handles special cases (e.g., "U.S.").
- **Done**: Finalizes the tokens.

![Tokenization Process](https://github.com/user-attachments/assets/0290e2da-669a-44e0-b865-06dae73aff0e)

## 3. Key Data Types in spaCy
Below are the primary data types used in spaCy for tokenization:

```python
type(sentence)  # <class 'spacy.tokens.doc.Doc'>
type(nlp)       # <class 'spacy.lang.en.English'>
type(token)     # <class 'spacy.tokens.token.Token'>
type(span)      # <class 'spacy.tokens.span.Span'>
```

- **Doc**: Represents the entire processed text.
- **Token**: Represents individual tokens.
- **Span**: Represents a slice of the `Doc` (e.g., a phrase or sentence).

## 4. Exploring Token Attributes
Use Python’s `dir()` function to explore the methods and attributes of a token:

```python
print(dir(token))
```

Example output:

```
[...
 'is_alpha',
 'is_ascii',
 'is_currency',
 'is_digit',
 'is_lower',
 'is_oov',
 'is_punct',
 ...]
```

### Common Attributes:
- **`is_alpha`**: Checks if the token is alphabetic.
- **`is_digit`**: Checks if the token is numeric.
- **`is_punct`**: Checks if the token is punctuation.
- **`is_oov`**: Indicates if the token is out-of-vocabulary.

## 5. Additional Resources
For a hands-on demonstration, refer to the accompanying Colab notebook:

[Relevant Colab Notebook](https://colab.research.google.com/drive/1r2N0WqjKLxJ3HEHIHDO08Aiw58AvTiDk?usp=sharing)

---
This tutorial is a foundational step in understanding tokenization with spaCy. Experiment with different sentences and attributes to explore its full potential!

