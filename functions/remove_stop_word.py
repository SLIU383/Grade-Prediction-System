import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def remove_stop_words(text):
    """
    Removes stop words from the input text.

    Parameters:
    text (str): The input text string from which stop words need to be removed.

    Returns:
    str: The text string with stop words removed.
    """
    tokens = word_tokenize(text)
    filtered_text = [word for word in tokens if word.lower() not in stop_words]
    filtered_text = ' '.join(filtered_text)
    return filtered_text