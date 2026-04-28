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

## 📂 Repository Structure

Below is the organization of the files within this repository:

```text
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

##🛡️ IPR Submission Proof
Score_Card.pdf: Official scoring and certification document for the project.

fake-news-detection-on-social-media...: Documentation providing proof of intellectual property submission.

##📝 Report and PPT
COOP2-Project Report .docx: The comprehensive project report detailing the methodology, literature review, and findings.

PPT_Research.pptx: The official presentation deck used to showcase the research and results.

##💻 Source Code
baseline_models.py: Python script used to train and evaluate baseline Machine Learning models, including Naive Bayes, Logistic Regression, and SVM.

generate_metrics.py: The primary script for training the Passive Aggressive Classifier and generating detailed performance metrics.

##🛠️ Tech Stack
Language: Python

Libraries: Scikit-learn, Pandas, NumPy, NLTK

Algorithm: Passive Aggressive Classifier

Vectorization: TF-IDF (Term Frequency-Inverse Document Frequency)

##📄 README.md: The main documentation file providing an overview and instructions for the repository.
---
---

## 💾 Dataset Installation (Important)

Due to GitHub's file size limits, the datasets are hosted externally on Google Drive. You must download them before running the code.

1. **Download the Data:** Click [this Google Drive Link](https://your-link-here) to access the datasets.
2. **Extract:** Download both `True.csv` and `Fake.csv`.
3. **Placement:** Move both downloaded `.csv` files directly into the same folder as your Python scripts.

---

## ⚙️ Prerequisites & Setup

Ensure you have Python 3.8+ installed on your system.

### 1. Clone the repository:
```bash
git clone [https://github.com/Adarsh-250/Fake_news_detection_Research_paper.git](https://github.com/Adarsh-250/Fake_news_detection_Research_paper.git)
cd Fake_news_detection_Research_paper
2. Install dependencies:
Bash

Bash
pip install -r requirements.txt
3. NLTK Stopwords Setup:
The scripts require the NLTK stopwords dataset to clean the text. Run this quick Python snippet to ensure they are downloaded:

Python

Python
import nltk
nltk.download('stopwords')
🚀 Running the Project
1️⃣ Baseline Models Evaluation
Train the Multinomial Naive Bayes, Logistic Regression, and SVM models. This script handles text preprocessing and provides comparative results.

Bash

Bash
python baseline_models.py
2️⃣ Passive Aggressive Classifier Evaluation
Train the primary PAC model to generate a detailed classification report and confusion matrix.

Bash

Bash
python generate_metrics.py

### 💡 Tips for editing:
* **Google Drive Link:** Replace `(https://your-link-here)` with your actual shared link.
* **Spacing:** I added horizontal rules (`---`) to match the clean separation seen in your screenshots.
* **Icons:** I used the exact emojis (💾, ⚙️, 🚀, 1️⃣, 2️⃣) to keep the visual style consistent.
