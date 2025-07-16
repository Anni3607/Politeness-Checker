### Politeness Checker - ML Project

This is a basic machine learning project that detects whether a given sentence is polite or impolite. It uses traditional NLP techniques like TF-IDF for feature extraction and logistic regression for classification.

The project is built using scikit-learn and deployed using Streamlit for easy interaction.

### What this project does

You can enter any sentence (like "Can you please help me?" or "Get lost.") and the model will classify it as either polite or impolite. The goal is to give quick feedback on tone in a lightweight interface.

#### How it works

1. A small, manually created dataset of 50 sentences (25 polite, 25 impolite) is used to train the model.
2. The input sentence is transformed into numerical form using TF-IDF.
3. Logistic regression is used to classify the sentence.
4. A Streamlit app serves as the front-end, where users can input text and receive results instantly.


#### Files included

* `politeness_model.pkl`: The trained machine learning model.
* `app.py`: Streamlit code that handles user input and shows predictions.
* `requirements.txt`: Python dependencies needed to run the app.



#### Notes

* The model is basic and works well for short, clear sentences.
* It might not handle sarcasm or subtle tones accurately.
* For better performance, the dataset can be expanded and more advanced models like BERT can be used.


