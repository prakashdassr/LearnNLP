To tokenize text in encoded form using Huggingface's Transformers package, you can use a pre-trained tokenizer provided by Huggingface. Here's an example:

[Colab link](https://colab.research.google.com/drive/1ZiaAO61tQfSu3ij9e5Y6_ulgah1eXrGC?usp=sharing)

### Steps:
1. **Install the Transformers Package**:
   If not already installed, you can install it using:
   ```bash
   pip install transformers
   ```

2. **Use a Pre-trained Tokenizer**:
   We'll use the tokenizer for a pre-trained model like `bert-base-uncased`.

3. **Tokenize and Encode**:
   Use the tokenizer's `encode` or `__call__` method to tokenize the text and convert it to token IDs.

### Example Code:

```python
from transformers import AutoTokenizer

# Load the tokenizer for a pre-trained model (e.g., BERT)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Input text
text = "He being a better guy, who eats apple as an everyday routine."

# Tokenize and encode the text
encoded = tokenizer(text, return_tensors="pt")  # Convert to PyTorch tensors
tokens = tokenizer.tokenize(text)  # Tokenized words
ids = encoded["input_ids"]  # Token IDs

# Print the results
print("Tokenized Text:", tokens)
print("Token IDs:", ids)
```

### Output:
For the input text:
```
"He being a better guy, who eats apple as an everyday routine."
```

The output might look like this:

#### Tokenized Text:
```text
['he', 'being', 'a', 'better', 'guy', ',', 'who', 'eats', 'apple', 'as', 'an', 'everyday', 'routine', '.']
```

#### Token IDs:
```text
tensor([[ 101, 2002, 2108, 1037, 2488, 3124, 1010, 2040, 9779, 6207, 2004, 2019, 7972, 12517, 1012, 102]])
```

### Explanation:
1. **Tokenized Text**: Breaks down the text into tokens (subwords, words, or punctuation).
2. **Token IDs**: Each token is mapped to a unique ID from the tokenizer's vocabulary.
3. **Special Tokens**:
   - `[CLS]` (ID: 101): Indicates the start of a sequence.
   - `[SEP]` (ID: 102): Marks the end of a sequence.

### Notes:
- Replace `"bert-base-uncased"` with the name of another pre-trained model if you want to use a different tokenizer.
- You can set additional options like `padding=True` and `truncation=True` to handle varying lengths of input.

Would you like to customize this further or test it with another model?
