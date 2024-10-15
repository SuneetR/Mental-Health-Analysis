from flask import Flask, request, jsonify, render_template
from chatbot import get_chatbot_response  # Import chatbot logic

app = Flask(__name__)

# Serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_response = get_chatbot_response(user_message)  # Get response from chatbot
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
