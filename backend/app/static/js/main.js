document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chatForm');
    const userInput = document.getElementById('userInput');
    const messageArea = document.getElementById('messageArea');

    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const question = userInput.value.trim();
        if (!question) return;

        // Add user message to chat
        addMessage('user', question);
        userInput.value = '';

        try {
            // Show loading message
            const loadingId = addMessage('bot', 'Thinking...');
            
            // Send request to backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question: question })
            });

            const data = await response.json();
            
            // Remove loading message and add bot response
            removeMessage(loadingId);
            addMessage('bot', data.answer);

        } catch (error) {
            console.error('Error:', error);
            addMessage('bot', 'Sorry, I encountered an error. Please try again.');
        }
    });

    function addMessage(type, content) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${type}-message`);
        messageDiv.textContent = content;
        
        const id = Date.now();
        messageDiv.setAttribute('data-id', id);
        
        messageArea.appendChild(messageDiv);
        messageArea.scrollTop = messageArea.scrollHeight;
        
        return id;
    }

    function removeMessage(id) {
        const message = messageArea.querySelector(`[data-id="${id}"]`);
        if (message) {
            message.remove();
        }
    }
});