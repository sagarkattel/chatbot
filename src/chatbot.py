import os
import re
import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_DIR = "models"

class MedicalChatbot:
    def __init__(self, model_dir=MODEL_DIR):
        self.model_dir = model_dir
        self.is_loaded = False
        self.questions = []
        self.answers = []
        self.vectorizer = None
        self.tfidf_matrix = None
        
        # Simple intent-based responses for small talk to guarantee smooth conversational experience
        self.conversational_responses = {
            "greetings": [
                r"\b(hi|hello|hey|g'day|hola|greetings)\b",
                "Hello! I am your AI medical assistant. How can I help you today?"
            ],
            "farewells": [
                r"\b(bye|goodbye|see you|farewell|quit|exit)\b",
                "Goodbye! Take care of yourself and stay healthy."
            ],
            "gratitude": [
                r"\b(thanks|thank you|appreciate it|helpful)\b",
                "You are very welcome! Let me know if you have any other questions."
            ],
            "identity": [
                r"\b(who are you|your name|what are you|what is your name)\b",
                "I am Medibot, an expert medical chatbot designed to provide information on symptoms, treatments, and general health queries."
            ],
            "capabilities": [
                r"\b(what can you do|help|capabilities|how to use|features)\b",
                "I can answer questions about common medical conditions, symptoms, treatments, and drug info. Simply ask me about a disease, symptom, or treatment!"
            ]
        }

    def clean_and_normalize(self, text):
        """Standardizes text and maps medical synonyms/singulars/plurals for high TF-IDF matching accuracy."""
        text = text.lower().strip()
        # Map general hypertension to high blood pressure (avoiding pulmonary)
        if "hypertension" in text and "pulmonary" not in text:
            text = text.replace("hypertension", "high blood pressure")
        # Normalize key query terms to singular or plural targets
        text = re.sub(r'\btreatment\b', 'treatments', text)
        text = re.sub(r'\bcause\b', 'causes', text)
        text = re.sub(r'\bsymptom\b', 'symptoms', text)
        text = re.sub(r'\bprevent\b', 'prevention', text)
        text = re.sub(r'\bdiagnose\b', 'diagnosis', text)
        return text

    def load_model(self):
        """Loads data, fits TF-IDF vectorizer for semantic retrieval."""
        if self.is_loaded:
            return
            
        csv_path = os.path.join("data", "medDataset_processed.csv")
        if not os.path.exists(csv_path):
            print("Dataset not found locally. Downloading...")
            os.makedirs("data", exist_ok=True)
            url = "https://huggingface.co/datasets/keivalya/MedQuad-MedicalQnADataset/resolve/main/medDataset_processed.csv"
            import urllib.request
            urllib.request.urlretrieve(url, csv_path)
            
        print("Loading dataset...")
        df = pd.read_csv(csv_path)
        df.rename(columns={"Question": "question", "Answer": "answer"}, inplace=True, errors="ignore")
        df = df.dropna(subset=["question", "answer"])
        
        self.questions = df["question"].tolist()
        self.answers = df["answer"].tolist()
        
        print("Fitting TF-IDF Vectorizer...")
        normalized_questions = [self.clean_and_normalize(q) for q in self.questions]
        
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(normalized_questions)
        self.is_loaded = True
        print("Retrieval index loaded successfully.")

    def check_conversational_triggers(self, query):
        """Checks if query is a simple greeting or common conversation trigger."""
        cleaned_query = query.lower().strip()
        cleaned_query = re.sub(f"[{re.escape(string.punctuation)}]", "", cleaned_query)
        
        for intent, (pattern, response) in self.conversational_responses.items():
            if re.search(pattern, cleaned_query):
                return response
        return None

    def generate_response(self, user_query):
        """Returns (short_answer, full_answer) tuple using TF-IDF retrieval."""
        if not self.is_loaded:
            self.load_model()

        # Normalize the user query
        processed_query = self.clean_and_normalize(user_query)

        # Compute similarities
        query_vec = self.vectorizer.transform([processed_query])
        similarity = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        best_match_idx = similarity.argsort()[-1]
        best_score = similarity[best_match_idx]

        # Low similarity fallback
        if best_score < 0.15:
            msg = "I am sorry, but I do not have information on that specific medical query. Please consult a healthcare professional."
            return msg, msg

        raw_answer = self.answers[best_match_idx]

        # Clean up excessive whitespace
        full = re.sub(r'\n{3,}', '\n\n', raw_answer)
        full = re.sub(r'[ \t]+', ' ', full).strip()

        # Build short answer: first 2 sentences, capped at 300 chars
        sentences = re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', full))
        sentences = [s.strip() for s in sentences if len(s.strip()) > 5]
        short = ' '.join(sentences[:2])
        if len(short) > 320:
            short = short[:317].rstrip() + '…'

        return short, full


    def get_response(self, user_query):
        """Main interface. Returns (short_answer, full_answer) tuple."""
        # 1. Routing for greeting / conversation
        conv_response = self.check_conversational_triggers(user_query)
        if conv_response:
            return conv_response, conv_response   # same for both short & full

        # 2. Medical Q&A using Retrieval
        try:
            return self.generate_response(user_query)
        except Exception as e:
            print(f"Error during response retrieval: {e}")
            msg = "I am experiencing technical issues retrieving an answer right now. Please seek medical advice from a doctor."
            return msg, msg


if __name__ == "__main__":
    # Quick CLI test
    chatbot = MedicalChatbot()
    print("Initializing CLI Test Mode. Loading model...")
    try:
        chatbot.load_model()
        print("\nType a message to test (type 'exit' to quit):")
        while True:
            query = input("User: ")
            if query.lower() in ["exit", "quit"]:
                break
            response = chatbot.get_response(query)
            print(f"Bot: {response}\n")
    except Exception as e:
        print(f"Failed to test chatbot: {e}")
