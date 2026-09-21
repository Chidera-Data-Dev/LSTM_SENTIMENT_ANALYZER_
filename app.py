import streamlit as st
import httpx

url = "https://lstm-sentiment-analyzer.onrender.com/api/sentiment_analysis/v1/predict"


def predict_sentiment(payload):
    with httpx.Client(timeout=30) as client:
        response = client.post(url, json=payload)
        response.raise_for_status()
        return response
    


st.set_page_config(
    page_title="Movie Sentiment Analyzer",
    page_icon="🎬",
    layout="wide"
)

st.markdown("# 🍿Movie Sentiment Analyzer")

# ======================================================
# CUSTOM CSS (FIXED VISIBILITY + MODERN UI)
# ======================================================
st.markdown("""
<style>

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ff512f, #dd2476);
    color: white;
    border-radius: 14px;
    font-size: 18px;
    padding: 12px 26px;
    font-weight: 700;
    border: none;
}
.stButton > button:hover {
    transform: scale(1.05);
}

/* Text input */
textarea {
    border-radius: 14px !important;
    border: 2px solid #93c5fd !important;
    background-color: #0f141c !important;
    color: #e2e8f0 !important;

    font-size: 16px !important;
}

</style>
""", unsafe_allow_html=True)

text = st.text_area("Enter your text here:", placeholder="Type something...", height=200)

st.button("PREDICT")

if text.strip() == "":
        st.warning("Please enter some text before clicking predict.")
else:
        payload = {"text": text}
        processing = st.info("Processing your text...")
        response = predict_sentiment(payload=payload).json()
        processing.empty()
        sentiment = response.get("sentiment").casefold()
        st.success("Done! Analysis complete.")
        st.markdown(f"You have a {sentiment} sentiment")
