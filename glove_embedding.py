GLOVE_EMBEDDING_PATH = '/content/gdrive/My Drive/Kaggle/COVID-19_Sentiment_Analysis/glove.840B.300d.txt'

word_index = len(tokenizer.word_index)

def get_coefs(word, *arr):
    """
    Return a tuple (word, embedding_vector).
    """
    return word, np.asarray(arr, dtype='float32')

def load_embeddings(path):
    """
    Return dictionary with entries of type {word:embedding_vector}.
    """
    with open(path) as file:
        return dict(get_coefs(*line.strip().split(' ')) for line in tqdm(file))
    
def build_matrix(word_index, path):
    """
    Build embedding matrix. Rows represent words according to their index in the vocab. Columns represent the embedding dimensions.
    """
    embedding_index = load_embeddings(path)
    embedding_matrix = np.zeros((len(word_index) + 1, 300))
    
    unknown_words = []
    for word, i in word_index.items():
        try:
            embedding_matrix[i] = embedding_index[word]
        except KeyError:
            unknown_words.append(word)
    return embedding_matrix, unknown_words
