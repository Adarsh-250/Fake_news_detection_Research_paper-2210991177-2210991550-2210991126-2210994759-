<h1 align="center">🕵️‍♂️ Fake News Detection on Social Media Platforms using NLP and PAC </h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Library-Scikit--Learn-orange.svg" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/NLP-NLTK-green.svg" alt="NLTK">
  <img src="https://img.shields.io/badge/Status-Published-success.svg" alt="Status">
</div>

<br>

## 📋 Project Metadata
* **Project Title:** Fake News Detection on Social Media Platforms using Natural Language Processing and Passive Aggressive Classifier
* **Type:** Research Paper
* **Current Status:** Completed and Published (DOI: 10.17577/IJERTV15IS031812)
* **Supervisor:** Dr. Ajay Katiyar
* **Team Details:**
    | Name | Roll Number |
    | :--- | :--- |
    | Adarsh Kumar Gupta | 2210991177 |
    | Drishti Monga | 2210991550 |
    | Aastha | 2210991126 |
    | Ankita Bansal | 2210994759 |

---

> **Overview:** This repository contains the source code and the final research paper for the detection of fake news using advanced Natural Language Processing (NLP) techniques. The project utilizes TF-IDF vectorization alongside a Passive Aggressive Classifier to achieve an accuracy of **99.59%** in distinguishing between legitimate and fake news articles.

---


📂 Repository Components
As per the evaluation requirements, this repository contains:

📁 IPR submission Proof:

📄 Score_Card.pdf: Official scoring or certification document.

📄 fake-news-detection-on-social-...: Proof of intellectual property submission related to the project.

📁 Report and PPT:

📄 COOP2-Project Report .docx: The detailed project report document.

📊 PPT_Research.pptx: The presentation deck covering the research findings.

📁 Source Code:

🐍 baseline_models.py: Script to train and evaluate baseline ML models (Naive Bayes, Logistic Regression, SVM).

🐍 generate_metrics.py: Script to train and evaluate the Passive Aggressive Classifier and generate performance metrics.

📄 README.md: The main documentation file providing an overview and instructions for the repository.
---

## 💾 Dataset Installation (Important)

Due to GitHub's file size limits, the datasets are hosted externally. You must download them before running the code.

1.  **Download the Data:** Click [this Google Drive Link](https://drive.google.com/drive/folders/1LaTPNj8HdWASmIPh6iVEJsKDPPXd3i9b?usp=sharing) to access the datasets.
2.  **Extract:** Download both `True.csv` and `Fake.csv`.
3.  **Placement:** Move both downloaded `.csv` files directly into the same folder as your Python scripts.

---

## ⚙️ Prerequisites & Setup

Ensure you have Python 3.9 installed on your system. 

**1. Clone the repository:**
```bash
git clone [https://github.com/Adarsh-250/Fake_news_detection_Research_paper.git](https://github.com/Adarsh-250/Fake_news_detection_Research_paper.git)
cd Fake_news_detection_Research_paper
2. Install dependencies:

Bash
pip install -r requirements.txt
3. NLTK Stopwords Setup:
The scripts require the NLTK stopwords dataset to clean the text. Run this Python snippet to ensure it is downloaded:

Python
import nltk
nltk.download('stopwords')
🚀 Running the Project
1️⃣ Baseline Models Evaluation
Train the Multinomial Naive Bayes, Logistic Regression, and SVM models. This script handles text preprocessing (URL removal, HTML tag stripping, and stopword removal) before running the TF-IDF vectorizer.

Bash
python baseline_models.py
2️⃣ Passive Aggressive Classifier Evaluation
Train the primary PAC model to generate a detailed classification report and confusion matrix.

Bash
python generate_metrics.py
