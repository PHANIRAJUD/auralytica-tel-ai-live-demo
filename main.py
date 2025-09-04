from preprocessing_agent import preprocess
from sentiment_analysis_agent import classify_sentiment
from insight_extraction_agent import extract_insights
from visualization_agent import visualize

feedback_samples = [
    "Good support experience",
    "Bad service and rude staff"
]

results = {"positive": 0, "negative": 0}

for feedback in feedback_samples:
    clean = preprocess(feedback)
    sentiment = classify_sentiment(clean)
    results[sentiment] += 1
    print(f"Feedback: {feedback}, Sentiment: {sentiment}, Insights: {extract_insights(clean)}")

visualize(results)