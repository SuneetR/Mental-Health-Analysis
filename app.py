# app.py
from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize Flask app
app = Flask(__name__)

# Initialize NLTK's VADER Sentiment Analyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    user_input = request.form['message']
    sentiment_score = sid.polarity_scores(user_input)
    
    # Determine sentiment based on compound score
    if sentiment_score['compound'] >= 0.05:
        sentiment = "positive"
        response = "I'm glad you're feeling positive!"
    elif sentiment_score['compound'] <= -0.05:
        sentiment = "negative"
        response = "I'm sorry you're feeling down. It's okay to talk about how you feel."
    else:
        sentiment = "neutral"
        response = "It sounds like you're feeling neutral. If there's more on your mind, feel free to share."

    return jsonify({
        'sentiment': sentiment,
        'response': response
    })

if __name__ == '__main__':
    app.run(debug=True)
