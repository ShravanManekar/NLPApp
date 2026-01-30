# 🧠 NLPApp – Offline Natural Language Processing Desktop Application

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white) 
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-brightgreen) 
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-orange) 
![spaCy](https://img.shields.io/badge/spaCy-NLP-red) 
![License](https://img.shields.io/badge/License-MIT-green)

**NLPApp** is a Python desktop application for performing Natural Language Processing (NLP) tasks **offline**, without requiring paid APIs or internet access. Built with **Tkinter**, **Hugging Face Transformers**, and **spaCy**, NLPApp demonstrates a production-ready NLP workflow with GUI integration.

---

## 🌟 Features

- **Sentiment Analysis** – Classifies text as Positive / Negative with confidence score  
- **Emotion Detection** – Detects emotions like anger, joy, sadness, fear, surprise, etc.  
- **Named Entity Recognition (NER)** – Extracts entities such as Person, Organization, Location, Date  
- **Interactive GUI** – Simple, user-friendly **Tkinter interface**  
- **Offline Execution** – Fully functional without internet or API keys after setup  

---

## 🛠 Tech Stack

- **Python 3**  
- **Tkinter** – Desktop GUI  
- **Hugging Face Transformers**  
  - `distilbert-base-uncased-finetuned-sst-2-english` (Sentiment Analysis)  
  - `emotion-english-distilroberta-base` (Emotion Detection)  
- **spaCy** – Named Entity Recognition  
- **Git & GitHub** – Version control  

---

## 📂 Project Structure

NLPApp/
│
├── app.py # Main Tkinter application
├── myapi.py # NLP logic (Sentiment, Emotion, NER)
├── mydb.py # User authentication
├── db.json # Local user database
├── resourse/ # Icons, images, and other assets
├── README.md
├── requirements.txt
├── .gitignore

## 🚀 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/ShravanManekar/NLPApp.git
cd NLPApp

2. **Create & activate a virtual environment**
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

3. **Install dependencies**
pip install -r requirements.txt
python -m spacy download en_core_web_sm

4. **Run the application**
python app.py

🧪 Example Outputs

Sentiment Analysis

Input: I love this application!
Output: 
Sentiment: POSITIVE
Confidence: 0.99


Emotion Detection

Input: I am very angry today
Output:
anger: 0.87
sadness: 0.05
joy: 0.03


Named Entity Recognition (NER)

Input: Apple was founded by Steve Jobs in California.
Output:
Apple → ORG
Steve Jobs → PERSON
California → GPE

🎯 Benefits

Demonstrates offline NLP model usage

Avoids paid APIs and rate limits

Combines AI + GUI development

Ideal for internships, portfolios, and resumes

📌 Future Improvements

Add file-based text input (TXT, CSV, PDF)

Export results as PDF/CSV

Implement dark mode UI

Compare model performance

👨‍💻 Author

Shravan Manekar

Computer Engineering Student

Interests: Data Science, NLP, AI

GitHub: https://github.com/ShravanManekar
