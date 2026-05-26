# Medibot AI 🩺

Medibot AI is a premium, modern, and clinically accurate conversational agent. It uses a **TF-IDF Hybrid Semantic Retrieval** system trained on the medical Q&A **MedQuAD** dataset. The application provides instant answers to user queries, returning concise summaries first with the option to expand and view the complete detail.

---

## ✨ Features

- **💡 Expandable Answers:** Shows a clean, 2-sentence summary first, keeping the conversation brief and readable. Users can click **📖 Expand for full answer** to see the complete detailed explanation.
- **🎨 Premium UI Design:** A beautiful dark-themed interface built using Streamlit, featuring glowing glassmorphism containers, radial background auras, and clean typography.
- **🧠 Query Normalization:** Normalizes user queries using custom mapping (e.g., synonyms like *hypertension* $\rightarrow$ *high blood pressure*, lemmatizations like *symptom* $\rightarrow$ *symptoms*) to guarantee high semantic similarity matching.
- **⚙️ Optimized Engine:** Runs on a fast vector similarity matching engine that matches user intent directly with the clinical dataset.

---

## 📂 Project Structure

```
├── data/
│   └── medDataset_processed.csv   # Dataset (auto-downloaded on first run)
├── src/
│   ├── app.py                     # Streamlit frontend application & UI
│   └── chatbot.py                 # Hybrid Retrieval chatbot logic
├── run.py                         # Environment-aware launcher script
├── requirements.txt               # Main dependencies
└── .gitignore                     # Git exclusion rules
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.10+** installed on your system.

### Running the App

You can start the app directly using the launcher script, which automatically detects your virtual environment (supports WSL/Linux and Windows native runtimes):

```bash
python run.py
```

Alternatively, you can run Streamlit manually:

```bash
# Activate your virtual environment
source venv_wsl/bin/activate   # Linux/WSL
# or
venv\Scripts\activate          # Windows

# Start Streamlit
streamlit run src/app.py
```

Once started, open your browser and navigate to:
👉 **`http://localhost:8502`** (or the port shown in your terminal).

---

## 🛠️ Built With

- **[Streamlit](https://streamlit.io/)** - Modern frontend web framework for data apps.
- **[Scikit-learn](https://scikit-learn.org/)** - TF-IDF Vectorization & Cosine Similarity.
- **[Pandas](https://pandas.pydata.org/)** - High-performance dataset parsing.
- **[MedQuAD Dataset](https://huggingface.co/datasets/keivalya/MedQuad-MedicalQnADataset)** - Medical Q&A dataset containing hundreds of verified disease and treatment definitions.

---

## ⚠️ Medical Disclaimer

Medibot is an educational project powered by a hybrid retrieval model trained on public medical QA pairs. It does not provide professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for personal health concerns.
