🧠 NLPApp – Offline NLP Desktop Application

NLPApp is a Python-based desktop application built using Tkinter, Hugging Face Transformers, and spaCy.
It performs Natural Language Processing tasks completely offline, without relying on paid or rate-limited APIs.

This project was built to understand real-world NLP workflows, GUI integration, and model inference in a production-like setup.

✨ Features

✅ Sentiment Analysis (Positive / Negative with confidence score)

😊 Emotion Detection (anger, joy, sadness, fear, surprise, etc.)

🏷 Named Entity Recognition (NER)

Detects Person, Organization, Location, Date, etc.

🖥 Simple & interactive Tkinter GUI

🔒 Offline execution (No API keys, no internet dependency after setup)

🛠 Tech Stack

Python 3

Tkinter – Desktop GUI

Hugging Face Transformers

distilbert-base-uncased-finetuned-sst-2-english (Sentiment)

emotion-english-distilroberta-base (Emotion Detection)

spaCy – Named Entity Recognition

Git & GitHub – Version control

📂 Project Structure
NLPApp/
│
├── app.py          # Main Tkinter application
├── myapi.py        # NLP logic (Sentiment, Emotion, NER)
├── mydb.py         # User authentication logic
├── db.json         # Local user database
├── resourse/       # App resources (icons/images)
├── README.md
├── .gitignore

🚀 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/ShravanManekar/NLPApp.git
cd NLPApp

2️⃣ Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

▶ How to Run
python app.py


The GUI window will open on your desktop.

🧪 Example Outputs
🔹 Sentiment Analysis

Input:

I love this application!


Output:

Sentiment: POSITIVE
Confidence: 0.99

🔹 Emotion Detection

Input:

I am very angry today


Output:

anger: 0.87
sadness: 0.05
joy: 0.03

🔹 Named Entity Recognition (NER)

Input:

Apple was founded by Steve Jobs in California.


Output:

Apple → ORG
Steve Jobs → PERSON
California → GPE

🎯 Why This Project?

Avoids paid NLP APIs and rate limits

Demonstrates offline ML model usage

Combines AI + GUI development

Ideal for internships, portfolios, and resumes

📌 Future Improvements

 Add file-based text input

 Export results as PDF/CSV

 Dark mode UI

 Model performance comparison

👨‍💻 Author

Shravan Manekar
📌 Computer Engineering Student
📌 Interested in Data Science, NLP & AI

🔗 GitHub: https://github.com/ShravanManekar

⭐ If you like this project, don’t forget to star the repository!
