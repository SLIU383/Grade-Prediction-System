import numpy as np
from functions.get_bert_embedding import get_bert_embeddings
import joblib

def predict_grade(feedback_sentences, sentiment_labels):
    # Step 1: Flatten feedback sentences and sentiments
    flattened_sentences = [sentence for paragraph in feedback_sentences for sentence in paragraph]
    flattened_sentiments = [sentiment for paragraph in sentiment_labels for sentiment in paragraph]

    # Step 2: Extract BERT embeddings for each sentence
    bert_embeddings = get_bert_embeddings(flattened_sentences)  # Replace with actual function to get embeddings

    # Step 3: Aggregate embeddings and sentiments by paragraphs
    # Assuming each paragraph corresponds to a feedback
    # Example aggregation: mean of BERT embeddings and sentiments for each paragraph

    start_idx = 0
    paragraph_embeddings = []
    for paragraph in feedback_sentences:
        num_sentences = len(paragraph)
        paragraph_embedding = np.mean(bert_embeddings[start_idx:start_idx + num_sentences], axis=0)
        paragraph_sentiment = np.mean(flattened_sentiments[start_idx:start_idx + num_sentences], axis=0)
        combined_features = np.hstack((paragraph_embedding, paragraph_sentiment))  # Combine BERT embeddings and sentiment
        paragraph_embeddings.append(combined_features)
        start_idx += num_sentences

    predict_text = np.array(paragraph_embeddings)

    voting_model = joblib.load('trained_models/voting_model_pred_grade2.pkl')
    voting_prediction = voting_model.predict(predict_text)
    return voting_prediction