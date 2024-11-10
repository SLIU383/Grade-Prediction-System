import numpy as np
import torch
from transformers import BertTokenizer, BertModel

def get_bert_embeddings(sentences):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    model.eval()

    embeddings = []
    
    with torch.no_grad():
        for sentence in sentences:
            # Tokenize the sentence
            inputs = tokenizer(sentence, return_tensors='pt', truncation=True, padding='max_length', max_length=128)
            outputs = model(**inputs)
            
            # Get the [CLS] token representation for the sentence (first token)
            cls_embedding = outputs.last_hidden_state[:, 0, :].squeeze().numpy()
            embeddings.append(cls_embedding)
    
    return np.array(embeddings)