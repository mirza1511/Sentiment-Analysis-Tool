😊 Sentiment Analyzer - Tkinter + Naive Bayes

A GUI-based Sentiment Analyzer built with Python, Tkinter, and Scikit-learn. It classifies user text as 'Positive' or 'Negative' using a Multinomial Naive Bayes model trained on 30 sample sentences.

✨ Features
- ML Based Classification: Uses `CountVectorizer` + `MultinomialNB` from scikit-learn
- Modern Dark UI: Card-style Tkinter interface with hover effects
- Real-time Prediction: Instant sentiment analysis on button click
- 30 Sample Dataset: 15 positive + 15 negative examples built-in
- Color Coded Output: 😊 Green for Positive, 😡 Red for Negative
- Input Validation: Shows warning if text box is empty

🖼️ Screenshot
<img width="494" height="377" alt="image" src="https://github.com/user-attachments/assets/6224a54a-b53f-42bc-8c83-66378b60ed43" />


🚀 How to Run
1. Install dependencies:
   ```bash
   pip install scikit-learn
2. Clone this repository:
   git clone https://github.com/mirza1511/Sentiment-Analyzer.git
3. Run the app:
   python sentiment_analyzer.py


💡 How to Use
1. Type any sentence in the input box
2. Click `Analyze Sentiment` or press `Enter`
3. See result: Positive or Negative

Try these examples:
      Input          |      Expected Output
I love this product  |  😊 Sentiment: Positive
This is terrible     |  😡 Sentiment: Negative
Best purchase ever   |  😊 Sentiment: Positive
Waste of money       |  😡 Sentiment: Negative


📋 Requirements
- Python 3.7+
- scikit-learn
- Tkinter (comes with Python)

🧠 How It Works
1. Vectorization: `CountVectorizer` converts text to bag-of-words features
2. Training: `MultinomialNB` trains on 30 labeled samples 
3. Prediction: New input text is vectorized and classified as positive/negative

🔧 Code Structure
Component | Purpose
`texts` + `labels` | 30-sample dataset for training
`CountVectorizer()` | Converts text to numerical features
`MultinomialNB()` | Naive Bayes classifier for text
`predict_sentiment()` | Takes input, predicts, updates GUI
Tkinter UI | Dark theme card with entry + button + label


⚠️ Limitations
This is a basic model for learning purposes:
- Only 30 training samples, so accuracy is limited
- Can't detect neutral sentiment
- No sarcasm/emoji handling
- Dataset is small, so unseen words may give wrong results

For better accuracy, use larger datasets like IMDB Reviews or Twitter data.

👨‍💻 Author
Mirza1511

