# AuralyTica Tel AI 🎧📊

**Customer Sentiment Analysis Using Agentic AI**

This project demonstrates an agentic architecture for analyzing customer feedback using NLP techniques and visualizing insights interactively with Streamlit.

---

## 🧠 Architecture

![Architecture Diagram](https://user-images.githubusercontent.com/placeholder/AuralyTica-Tel-AI-Architecture.png)

- **Preprocessing Agent** – Cleans and normalizes customer feedback
- **Sentiment Analysis Agent** – Classifies as positive/negative
- **Insight Extraction Agent** – Detects themes, emotion, and intensity
- **Visualization Agent** – Graphs and dashboards (via Streamlit UI)

---

## 🚀 Run Locally (Streamlit)

### Requirements
- Python 3.x
- `streamlit` (for frontend)
- `matplotlib` (for graph output, optional)

### Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Files Included

| File                        | Purpose                                  |
|-----------------------------|-------------------------------------------|
| `app.py`                   | Streamlit interface                      |
| `main.py`                  | CLI-based execution                      |
| `preprocessing_agent.py`   | Text cleaning logic                      |
| `sentiment_analysis_agent.py` | Basic rule-based sentiment engine     |
| `insight_extraction_agent.py` | Dummy emotion extractor                |
| `visualization_agent.py`   | Generates bar chart for CLI demo         |
| `README.md`                | Project documentation                    |
| `requirements.txt`         | Python dependencies                      |

---

## 🧪 Sample Output

```bash
Feedback: Good support experience
Sentiment: positive
Insights: {'themes': ['support'], 'emotion': 'happy', 'intensity': 'medium'}
```

---

## 🖥️ Screenshot

Coming soon...

---

## 📜 License

MIT License

---

## 🤖 Built with ❤️ using Python, NLP, Azure, LangChain