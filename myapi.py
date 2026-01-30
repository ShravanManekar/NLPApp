from transformers import pipeline
import spacy

class API:
    def __init__(self):
        # Sentiment model (fast & accurate)
        self.sentiment_model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

        # Emotion model
        self.emotion_model = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            return_all_scores=True
        )

        # NER model
        self.nlp = spacy.load("en_core_web_sm")

    def sentiment_result(self, text):
        return self.sentiment_model(text)

    def emotion_result(self, text):
        return self.emotion_model(text)

    def ner_result(self, text):
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]
