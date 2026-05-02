import tkinter as tk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# -------------------- DATASET (30 samples) --------------------

texts = [
    # Positive
    "I love this product",
    "This is amazing",
    "So good and nice",
    "Excellent quality",
    "Very happy with this",
    "I am satisfied",
    "Really good experience",
    "Totally love it",
    "Best purchase ever",
    "Highly recommended",
    "Works perfectly",
    "Super amazing product",
    "Very useful and good",
    "I am impressed",
    "Fantastic item",

    # Negative
    "I hate this",
    "Very bad experience",
    "Worst ever",
    "Not good",
    "Really disappointing",
    "I am not happy",
    "Waste of money",
    "Terrible quality",
    "Very poor product",
    "I dislike this",
    "Bad experience overall",
    "Totally useless",
    "Stopped working",
    "Broken and useless",
    "Not worth it"
]

labels = [
    "positive","positive","positive","positive","positive",
    "positive","positive","positive","positive","positive",
    "positive","positive","positive","positive","positive",
    "negative","negative","negative","negative","negative",
    "negative","negative","negative","negative","negative",
    "negative","negative","negative","negative","negative"
]

# -------------------- MODEL --------------------

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# -------------------- PREDICTION FUNCTION --------------------

def predict_sentiment():
    user_text = entry.get().strip().lower()

    if user_text == "":
        output_label.config(text="⚠️ Please enter text", fg="yellow")
        return

    vector = vectorizer.transform([user_text])
    result = model.predict(vector)[0]

    if result == "positive":
        output_label.config(text="😊 Sentiment: Positive", fg="#22c55e")
    else:
        output_label.config(text="😡 Sentiment: Negative", fg="#ef4444")

# -------------------- GUI (IMPROVED) --------------------

root = tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("500x350")
root.config(bg="#0f172a")
root.resizable(False, False)

# Main Frame (Card UI)
frame = tk.Frame(root, bg="#1e293b", padx=25, pady=25)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title = tk.Label(
    frame,
    text="😊 Sentiment Analyzer",
    font=("Arial", 18, "bold"),
    bg="#1e293b",
    fg="white"
)
title.pack(pady=10)

# Input box
entry = tk.Entry(
    frame,
    width=40,
    font=("Arial", 12),
    bg="#0f172a",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry.pack(pady=10, ipady=7)

# Button hover effects
def on_enter(e):
    btn.config(bg="#22c55e")

def on_leave(e):
    btn.config(bg="#16a34a")

# Button
btn = tk.Button(
    frame,
    text="Analyze Sentiment",
    command=predict_sentiment,
    font=("Arial", 11, "bold"),
    bg="#16a34a",
    fg="white",
    relief="flat",
    padx=12,
    pady=6
)
btn.pack(pady=10)

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Output label
output_label = tk.Label(
    frame,
    text="Enter text and click analyze",
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
)
output_label.pack(pady=15)

root.mainloop()