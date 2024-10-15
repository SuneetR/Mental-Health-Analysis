from textblob import TextBlob

def get_chatbot_response(user_message):
    # Analyze sentiment
    blob = TextBlob(user_message)
    sentiment = blob.sentiment.polarity

    # Generate a basic response based on sentiment
    if sentiment > 0:
        return "I'm glad to hear that! Keep up the positive vibes."
    elif sentiment < 0:
        return "I'm sorry you're feeling down. Do you want to talk more about it?"
    else:
        return "I understand. Let's talk more about how you're feeling."

