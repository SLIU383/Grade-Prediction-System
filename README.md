# Grade Prediction Application

A desktop application built with Python/Tkinter that processes student feedback and predicts grades using natural language processing and machine learning techniques.

## Features

- Text feedback processing with coreference resolution
- Sentiment analysis of feedback
- Automated grade prediction
- Interactive GUI interface
- Real-time process status updates
- Grade viewing and management system

## Prerequisites

- Python 3.x
- SQLite3
- fuzzywuzzy
- joblib
- matplotlib
- nltk
- numpy
- pandas
- pdfplumber
- Pillow
- scikit_learn
- torch
- tqdm
- transformers

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd grade-prediction-app
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure you have the necessary database structure:
```bash
database/
    └── assigned_feedback.db
    └── coreference_origin_text.db
    └── feedback_model_prediction.db
    └── student_grade.db
```

4. Ensure you have download the necessary models:
```bash
trained_models/
    └── sentiment_analysis.pth: clone from huggingface repository link: git clone git clone https://huggingface.co/ssssliu/sentiment_analysis
    └── feedback_extraction.pth: clone from huggingface repository link: git clone https://huggingface.co/ssssliu/feedback_extraction_model
    └── grade_prediction.pth: clone from huggingface repository link: git clone git clone https://huggingface.co/ssssliu/grade_prediction
```

## Project Structure

```
grade-prediction-app/
├── functions/
├── trained_models/
├── database/
└── main.py
```

## Usage

1. Launch the application:
```bash
python main_process.py
```

2. Using the interface:
   - Select the folder containing reflection documents
   - Choose the file (Excel format) containing team information
   - Click "Start Process" to begin the grade prediction
   - Use "View Grades" to see the predicted results after process finish

## Process Flow

1. **Coreference Resolution**: Processes text to resolve personal references
2. **Feedback Extraction**: Extracts relevant feedback information
3. **Sentiment Analysis**: Analyzes the sentiment of the feedback
4. **Grade Prediction**: Predicts final grades based on processed data



