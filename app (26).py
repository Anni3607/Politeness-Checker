
import streamlit as st
import joblib

model = joblib.load("politeness_model.pkl")

st.title("🗣️ Politeness Checker")
st.markdown("Enter a sentence to check whether it's polite or impolite.")

text_input = st.text_input("Your sentence:")

if text_input:
    prediction = model.predict([text_input])[0]
    emoji = "😊" if prediction == 1 else "😠"
    label = "Polite" if prediction == 1 else "Impolite"
    st.markdown(f"### Prediction: **{label}** {emoji}")
