import string
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

def preprocess(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])

    # Split into words
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stopwords.words('english')]

    return ' '.join(words)