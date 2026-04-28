<h1 align="center">🕵️‍♂️ Fake News Detection on Social Media Platforms using NLP and PAC </h1>

<div align="center">
  <img src="[https://img.shields.io/badge/Python-3.8+-blue.svg](https://img.shields.io/badge/Python-3.8+-blue.svg)" alt="Python">
  <img src="[https://img.shields.io/badge/Library-Scikit--Learn-orange.svg](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)" alt="Scikit-Learn">
  <img src="[https://img.shields.io/badge/NLP-NLTK-green.svg](https://img.shields.io/badge/NLP-NLTK-green.svg)" alt="NLTK">
  <img src="[https://img.shields.io/badge/Status-Evaluation_Ready-success.svg](https://img.shields.io/badge/Status-Evaluation_Ready-success.svg)" alt="Status">
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

> **Overview:** This repository contains the source code and the final research paper for the detection of fake news using advanced Natural Language Processing (NLP) techniques. The project utilizes TF-IDF vectorization alongside various machine learning classifiers to accurately classify news articles as legitimate or fake.

---

## 📂 Repository Structure

Below is the organization of the files within this repository:

```text
.
├── 📂 IPR submission Proof
│   ├── 📄 Score_Card.pdf
│   └── 📄 fake-news-detection-on-social-media...
├── 📂 Report and PPT
│   ├── 📄 COOP2-Project Report .docx
│   └── 📊 PPT_Research.pptx
├── 📂 Source Code
│   ├── 🐍 baseline_models.py
│   └── 🐍 generate_metrics.py
└── 📄 README.md
📑 Component Details
🛡️ IPR Submission Proof
Score_Card.pdf: Official scoring and certification document validating the project's performance.

fake-news-detection-on-social-media...: Official documentation providing proof of intellectual property submission.

📝 Report and PPT
COOP2-Project Report .docx: A comprehensive project report detailing the research methodology, literature review, and final findings.

PPT_Research.pptx: The official presentation deck used for demonstrating research insights and results.

💻 Source Code
baseline_models.py: Python script used to train and evaluate baseline Machine Learning models, including Naive Bayes, Logistic Regression, and SVM.

generate_metrics.py: The primary script for training the Passive Aggressive Classifier and generating high-accuracy performance metrics.

🛠️ Tech Stack
Category	Tools / Technologies
Language	Python
Libraries	Scikit-learn, Pandas, NumPy, NLTK
Algorithm	Passive Aggressive Classifier
Vectorization	TF-IDF (Term Frequency-Inverse Document Frequency)
💾 Dataset Installation (Important)
Due to GitHub's file size limits, the datasets are hosted externally on Google Drive. You must download them before running the code.

Download the Data: Click this Google Drive Link to access the datasets.

Extract: Download both True.csv and Fake.csv.

Placement: Move both downloaded .csv files directly into the same folder as your Python scripts.

⚙️ Prerequisites & Setup
Ensure you have Python 3.8+ installed on your system.

1. Clone the repository:
Bash
git clone https://github.com/Adarsh-250/Fake_news_detection_Research_paper.git
cd Fake_news_detection_Research_paper
2. Install dependencies:
Bash
pip install -r requirements.txt
3. NLTK Stopwords Setup:
The scripts require the NLTK stopwords dataset to clean the text. Run this quick Python snippet:

Python
import nltk
nltk.download('stopwords')
🚀 Running the Project
1️⃣ Baseline Models Evaluation
Train the Multinomial Naive Bayes, Logistic Regression, and SVM models. This script handles text preprocessing (URL removal, HTML tag stripping, etc.).

Bash
python baseline_models.py
2️⃣ Passive Aggressive Classifier Evaluation
Train the primary PAC model to generate a detailed classification report and confusion matrix.

Bash
python generate_metrics.py
