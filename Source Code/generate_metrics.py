import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Download NLTK stopwords 
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

# 1. Load the ISOT Dataset
true_df = pd.read_csv('True.csv')
fake_df = pd.read_csv('Fake.csv')

# Add labels: 1 for Legitimate (True), 0 for Fake
true_df['label'] = 1
fake_df['label'] = 0

# Combine datasets and shuffle (random_state ensures reproducible results)
df = pd.concat([true_df, fake_df], axis=0).sample(frac=1, random_state=42).reset_index(drop=True)

# Combine Title and Text 
df['full_text'] = df['title'] + " " + df['text']

# 2. NLP Preprocessing Pipeline
def clean_text(text):
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Apply the cleaning function 
df['clean_text'] = df['full_text'].apply(clean_text)

# 3. Train/Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(df['clean_text'], df['label'], test_size=0.20, random_state=42)

# 4. TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7, ngram_range=(1, 2))
tfidf_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_test = tfidf_vectorizer.transform(X_test)

# 5. Initialize and Train the PAC Model
pac = PassiveAggressiveClassifier(max_iter=50, random_state=42)
pac.fit(tfidf_train, y_train)

# 6. Predict and Evaluate
y_pred = pac.predict(tfidf_test)

# Calculate Metrics
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", classification_report(y_test, y_pred))





