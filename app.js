function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');

    // Display user message
    chatBox.innerHTML += `<p>You: ${userInput}</p>`;

    // Send message to Flask API
    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        chatBox.innerHTML += `<p>Bot: ${data.response}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    // Clear input field
    document.getElementById('user-input').value = '';
}
