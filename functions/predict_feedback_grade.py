import torch
from transformers import BertModel, BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import LabelEncoder
import numpy as np

class predict_sentences:
    def __init__(self, model_path):
        self.label_encoder = LabelEncoder()
        self.label_encoder.fit(['A', 'B', 'C', 'D'])
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=4)
        self.model.load_state_dict(torch.load(model_path), strict=False)
        self.model.eval()  # Set the model to evaluation mode

        # Load the tokenizer
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.model.to(self.device)

    def preprocess_feedback(self, feedback_sentences, sentiment_labels):
        # Combine each sentence with its sentiment label as a prefix
        feedback_text = " ".join(
            f"{'Positive' if label > 0 else 'Negative' if label < 0 else 'Neutral'}: {sentence}"
            for sentence, label in zip(feedback_sentences, sentiment_labels)
        )

        # Tokenize the concatenated feedback text
        encoding = self.tokenizer(
            feedback_text,
            padding="max_length",
            truncation=True,
            max_length=512,
            return_tensors="pt"
        )

        return encoding["input_ids"].to(self.device), encoding["attention_mask"].to(self.device)

    def predict_grade(self, feedback_sentences, sentiment_labels):
        self.model.eval()
        input_ids, attention_mask = self.preprocess_feedback(feedback_sentences, sentiment_labels)

        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            pred_class = torch.argmax(logits, dim=1).item()

        # Convert numeric prediction back to grade label
        predicted_grade = self.label_encoder.inverse_transform([pred_class])[0]
        return predicted_grade

# class predict_sentences:
#     def __init__(self, model_path):
#         # Load the trained BERT model
#         self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=4)
#         self.model.load_state_dict(torch.load(model_path), strict=False)
#         self.model.eval()  # Set the model to evaluation mode

#         # Load the tokenizer
#         self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
#         self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
#         self.model.to(self.device)

#     def tokenize_sentences(self, sentences):
#         encoded_inputs = self.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
#         return encoded_inputs

#     def predict_sentences(self, input_data):
#         encoded_inputs = self.tokenize_sentences(input_data)
#         input_ids = encoded_inputs['input_ids'].to(self.device)
#         attention_mask = encoded_inputs['attention_mask'].to(self.device)

#         dataset = TensorDataset(input_ids, attention_mask)
#         dataloader = DataLoader(dataset, batch_size=16, shuffle=False)

#         all_preds = []
#         self.model.eval()
#         with torch.no_grad():
#             for batch in dataloader:
#                 input_ids = batch[0].to(self.device)
#                 attention_mask = batch[1].to(self.device)
#                 outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
#                 logits = outputs.logits
#                 preds = torch.argmax(logits, dim=1).cpu().numpy()
#                 all_preds.extend(preds)
#         return all_preds