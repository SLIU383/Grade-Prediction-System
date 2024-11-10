import torch
from transformers import BertModel, BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader
from torch.utils.data import DataLoader, TensorDataset

class predict_sentences:
    def __init__(self, model_path):
        # Load the trained BERT model
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
        self.model.load_state_dict(torch.load(model_path),strict=False)
        self.model.eval()  # Set the model to evaluation mode

        # Load the tokenizer
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.model.to(self.device)

    def tokenize_sentences(self, sentences):
        encoded_inputs = self.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
        return encoded_inputs

    def predict_sentences(self, input_data):
        encoded_inputs = self.tokenize_sentences(input_data)
        input_ids = encoded_inputs['input_ids'].to(self.device)
        attention_mask = encoded_inputs['attention_mask'].to(self.device)

        dataset = TensorDataset(input_ids, attention_mask)
        dataloader = DataLoader(dataset, batch_size=16, shuffle=False)

        all_preds = []
        self.model.eval()
        with torch.no_grad():
            for batch in dataloader:
                input_ids = batch[0].to(self.device)
                attention_mask = batch[1].to(self.device)
                outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
                logits = outputs.logits
                preds = torch.argmax(logits, dim=1).cpu().numpy()
                all_preds.extend(preds)
        return all_preds