# StudyAus AI 🎓

StudyAus AI is a premium, modern, and highly helpful conversational guide designed for international students planning to study or currently studying in Australia. It uses a **TF-IDF Hybrid Semantic Retrieval** engine to provide instant, accurate answers about Australian visas, university selection, academic policies, assignments, attendance rules, and cultural integration.

---

## ✨ Features

- **💡 Expandable Answers:** Shows a clean, 2-sentence summary first, keeping the conversation brief and readable. Users can click **📖 Expand for full answer** to see the complete detailed explanation.
- **🎨 Premium UI Design:** A beautiful dark-themed interface built using Streamlit, featuring glowing glassmorphism containers, radial background auras, and clean typography.
- **🧠 Query Normalization:** Normalizes student and visa terminology (e.g. *uni* $\rightarrow$ *university*, *subclass 500* $\rightarrow$ *student visa*) to guarantee high semantic similarity matching.
- **🦘 Curated Knowledge Base:** Pre-loaded with answers covering crucial visa regulations (Subclass 500, 485), university intakes, grading systems, 80% attendance policies, academic integrity/plagiarism, cost of living, transport concessions, and cultural adjustment tips.

---

## 📂 Project Structure

```
├── data/
│   └── aus_student_dataset.csv    # Curated Q&A dataset
├── src/
│   ├── app.py                     # Streamlit frontend application & UI
│   └── chatbot.py                 # TF-IDF Retrieval chatbot engine
├── run.py                         # Environment-aware launcher script
├── requirements.txt               # Main dependencies
├── README.md                      # Project documentation
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

- **[Streamlit](https://streamlit.io/)** - Modern frontend web framework.
- **[Scikit-learn](https://scikit-learn.org/)** - TF-IDF Vectorization & Cosine Similarity.
- **[Pandas](https://pandas.pydata.org/)** - Dataset parsing.

---

## ⚠️ Education & Visa Disclaimer

StudyAus AI is an educational assistant providing general guide details compiled from public immigration and university policy documents. It is **not** legal immigration advice or official university advice. Always check official sources like [homeaffairs.gov.au](https://www.homeaffairs.gov.au/) or your university's official handbook.
