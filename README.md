<h1 align="center">🕵️‍♂️ Fake News Detection on Social Media Platforms using NLP and PAC </h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Library-Scikit--Learn-orange.svg" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/NLP-NLTK-green.svg" alt="NLTK">
  <img src="https://img.shields.io/badge/Status-Published-success.svg" alt="Status">
</div>

<br>

## 📋 Project Metadata
* [cite_start]**Project Title:** Fake News Detection on Social Media Platforms using Natural Language Processing and Passive Aggressive Classifier [cite: 933]
* [cite_start]**Type:** Research Paper [cite: 933]
* [cite_start]**Current Status:** Completed and Published (DOI: 10.17577/IJERTV15IS031812) [cite: 933-949]
* [cite_start]**Supervisor:** Dr. Ajay Katiyar [cite: 934]
* **Team Details:**
    | Name | Roll Number |
    | :--- | :--- |
    | Adarsh Kumar Gupta | 2210991177 |
    | Drishti Monga | 2210991550 |
    | Aastha | 2210991126 |
    | Ankita Bansal | 2210994759 |

[cite_start][cite: 934, 1342]

---

> [cite_start]**Overview:** This repository contains the source code and the final research paper for the detection of fake news using advanced Natural Language Processing (NLP) techniques[cite: 943]. [cite_start]The project utilizes TF-IDF vectorization alongside a Passive Aggressive Classifier to achieve an accuracy of **99.59%** in distinguishing between legitimate and fake news articles[cite: 945, 948].

---

## 📂 Repository Components

As per the evaluation requirements, this repository contains:
* [cite_start]📄 **Report:** `Research_Paper.pdf` - The final published research paper[cite: 1264].
* [cite_start]💻 **Source Code:** * `baseline_models.py`: Script to train and evaluate Baseline ML models (Naive Bayes, Logistic Regression, SVM) [cite: 1140-1144].
    * [cite_start]`generate_metrics.py`: Script to train and evaluate the Passive Aggressive Classifier [cite: 1311-1314].
* [cite_start]📊 **Datasets:** Required `.csv` files based on the ISOT Fake News Dataset[cite: 944, 1040].

---

## 💾 Dataset Installation (Important)

Due to GitHub's file size limits, the datasets are hosted externally. You must download them before running the code.

1.  **Download the Data:** Click [this Google Drive Link](https://drive.google.com/drive/folders/1LaTPNj8HdWASmIPh6iVEJsKDPPXd3i9b?usp=sharing) to access the datasets.
2.  [cite_start]**Extract:** Download both `True.csv` and `Fake.csv` [cite: 1284-1285].
3.  [cite_start]**Placement:** Move both downloaded `.csv` files directly into the same folder as your Python scripts[cite: 1283].

---

## ⚙️ Prerequisites & Setup

[cite_start]Ensure you have Python 3.9 installed on your system[cite: 1099]. 

**1. Clone the repository:**
```bash
git clone [https://github.com/Adarsh-250/Fake_news_detection_Research_paper.git](https://github.com/Adarsh-250/Fake_news_detection_Research_paper.git)
cd Fake_news_detection_Research_paper
2. Install dependencies:Bashpip install -r requirements.txt
3. NLTK Stopwords Setup:
The scripts require the NLTK stopwords dataset to clean the text. Run this Python snippet to ensure it is downloaded:  Pythonimport nltk
nltk.download('stopwords')
🚀 Running the Project1️⃣ Baseline Models EvaluationTrain the Multinomial Naive Bayes, Logistic Regression, and SVM models. This script handles text preprocessing (URL removal, HTML tag stripping, and stopword removal) before running the TF-IDF vectorizer .  Bashpython baseline_models.py
2️⃣ Passive Aggressive Classifier EvaluationTrain the primary PAC model to generate a detailed classification report and confusion matrix .  Bashpython generate_metrics.py

---

### Simplest Way to Update Your README
Since you want the "simplest way," follow these steps directly on the web:

1.  **Go to GitHub**: Open your repository in your browser.
2.  **Locate the File**: Click on the `README.md` file in your file list.
3.  **Enter Edit Mode**: Click the **Pencil Icon** (Edit this file) located at the top right of the file view.
4.  **Paste and Save**: Delete all the old code, paste the new block I provided above, and scroll down to click **Commit changes**.
