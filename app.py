import streamlit as st
from preprocessing_agent import preprocess
from sentiment_analysis_agent import classify_sentiment
from insight_extraction_agent import extract_insights

st.set_page_config(page_title="AuralyTica Tel AI", layout="centered")
st.title("AuralyTica Tel AI")
st.subheader("Customer Sentiment Analysis Using Agentic AI")

feedback = st.text_area("Enter Customer Feedback")

if st.button("Analyze"):
    if feedback.strip() == "":
        st.warning("Please enter some feedback text.")
    else:
        clean = preprocess(feedback)
        sentiment = classify_sentiment(clean)
        insights = extract_insights(clean)
        
        st.markdown(f"### Sentiment: `{sentiment.capitalize()}`")
        st.markdown("### Extracted Insights")
        st.json(insights)