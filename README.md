# Misinformation Detection using Natural Language Processing

## Overview
This repository contains the source code and the final research paper for the detection of fake news using NLP techniques. The project utilizes TF-IDF vectorization alongside various machine learning classifiers (Multinomial Naive Bayes, Logistic Regression, SVM, and Passive Aggressive Classifier) to classify news articles as legitimate or fake.

## Repository Components
As per the evaluation requirements, this repository contains:
1. **Report:** `Research_Paper.pdf` - The final published/submitted research paper.
2. **Source Code:** - `baseline_models.py`: Script to train and evaluate Baseline ML models (Naive Bayes, Logistic Regression, SVM).
   - `generate_metrics.py`: Script to train and evaluate the Passive Aggressive Classifier.
3. **Datasets:** Requires `True.csv` and `Fake.csv` in the root directory.

## Prerequisites & Installation
Ensure you have Python 3.8+ installed. 

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/Fake-News-Detection-NLP.git](https://github.com/yourusername/Fake-News-Detection-NLP.git)
   cd Fake-News-Detection-NLP
Install required dependencies:

Bash
pip install -r requirements.txt
NLTK Stopwords Setup:
The scripts require the NLTK stopwords dataset. It will attempt to download automatically, but you can manually ensure it is installed by running:

Python
import nltk
nltk.download('stopwords')
Running the Project
1. Baseline Models Evaluation
To train the Multinomial Naive Bayes, Logistic Regression, and SVM models and print their Accuracy, Precision, Recall, and F1-Scores:

Bash
python baseline_models.py
Note: The script handles text preprocessing (URL removal, HTML tag removal, punctuation stripping, and stopword removal) before TF-IDF vectorization.

2. Passive Aggressive Classifier (PAC) Evaluation
To train the PAC model and generate a detailed classification report and confusion matrix:

Bash
python generate_metrics.py
