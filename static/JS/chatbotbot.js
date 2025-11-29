// static/js/chatbot.js
document.addEventListener('DOMContentLoaded', function() {
    const chatbotButton = document.getElementById('chatbot-button');
    const chatbotContainer = document.getElementById('chatbot-container');
    const closeChatbot = document.getElementById('close-chatbot');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatMessages = document.getElementById('chatbot-messages');

    // Mostrar/ocultar el chat
    chatbotButton.addEventListener('click', () => {
        chatbotContainer.style.display = 'flex';
        chatbotButton.style.display = 'none';
    });

    closeChatbot.addEventListener('click', () => {
        chatbotContainer.style.display = 'none';
        chatbotButton.style.display = 'block';
    });

    // Enviar mensaje al presionar Enter
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Enviar mensaje al hacer clic en el botón
    sendButton.addEventListener('click', sendMessage);

    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;

        // Mostrar mensaje del usuario
        displayMessage(message, 'user');
        userInput.value = '';
        userInput.disabled = true;
        sendButton.disabled = true;

        try {
            // Mostrar indicador de carga
            const loadingId = 'loading-' + Date.now();
            displayMessage('<div class="typing-indicator"><span></span><span></span><span></span></div>', 'bot', loadingId);

            // Enviar mensaje al backend
            const response = await fetch('/api/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();

            // Eliminar indicador de carga
            const loadingElement = document.getElementById(loadingId);
            if (loadingElement) {
                loadingElement.remove();
            }

            // Mostrar respuesta
            displayMessage(data.response, 'bot');
        } catch (error) {
            console.error('Error:', error);
            displayMessage('Lo siento, hubo un error al procesar tu mensaje.', 'bot');
        } finally {
            userInput.disabled = false;
            sendButton.disabled = false;
            userInput.focus();
        }
    }

    function displayMessage(message, sender, customId = null) {
        const messageDiv = document.createElement('div');
        if (customId) messageDiv.id = customId;
        messageDiv.classList.add('message', `${sender}-message`);
        
        // Formatear el mensaje para mostrar enlaces y saltos de línea
        const formattedMessage = message
            .replace(/\n/g, '<br>')
            .replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank" style="color: #4CAF50; text-decoration: underline;">$1</a>');

        messageDiv.innerHTML = formattedMessage;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Función para obtener el token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Mensaje de bienvenida
    setTimeout(() => {
        displayMessage("¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte hoy?", 'bot');
    }, 1000);
});