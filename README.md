# Cure-Now Health Chatbot 🏥

An intelligent medical chatbot powered by Google's Gemini AI that provides accurate health-related information by leveraging a comprehensive medical knowledge base.

## Features 🌟

- **AI-Powered Responses**: Utilizes Google's Gemini AI for natural and accurate responses
- **Medical Knowledge Base**: Integrated with extensive medical documentation
- **Vector Search**: Uses Pinecone for efficient similarity search
- **User-Friendly Interface**: Clean and intuitive chat interface
- **Real-time Responses**: Instant answers to health-related queries

## Tech Stack 💻

- **Backend**: Python, Flask
- **AI/ML**: 
  - Google Gemini AI
  - LangChain
  - Hugging Face Embeddings
- **Vector Database**: Pinecone
- **Frontend**: HTML, CSS, JavaScript
- **Development Tools**: 
  - Python virtual environment
  - Git version control

## Prerequisites 📋

Before running the application, make sure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key
- Pinecone API key

## Installation 🛠️

1. Clone the repository
```bash
git clone https://github.com/Dadiya-Harsh/Cure-Now.git
cd cure-now
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your API keys
```env
GEMINI_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Usage 🚀

1. Start the Flask server
```bash
python backend/run.py
```

2. Open your web browser and navigate to
```
http://127.0.0.1:5000
```

3. Start chatting with the bot by typing your health-related questions in the chat interface

## Project Structure 📁

```
cure-now/
├── backend/
│   ├── app/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── routes.py
│   └── run.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Current Limitations ⚠️

- The chatbot's knowledge is limited to the medical documentation provided
- Responses are based on pre-processed medical information
- Not a substitute for professional medical advice

## Future Enhancements 🔮

- [ ] Enhanced medical knowledge base
- [ ] Multi-language support
- [ ] User authentication
- [ ] Chat history storage
- [ ] More interactive UI elements
- [ ] Response confidence scoring

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments 🙏

- Google Gemini AI for providing the language model
- Pinecone for vector similarity search
- Medical resources used in the knowledge base

## Disclaimer ⚖️

This chatbot is for informational purposes only and should not be considered as professional medical advice. Always consult with qualified healthcare providers for medical decisions.

---
Developed with ❤️ for better healthcare accessibility