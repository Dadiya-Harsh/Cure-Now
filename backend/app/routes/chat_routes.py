from flask import Blueprint, jsonify, render_template, request

from app.config import Config
from app.utils.embeddings import get_embeddings
from app.utils.pinecone_ops import initialize_pinecone, get_vector_store
from app.utils.gemini_ops import get_llm, create_qa_chain

chat = Blueprint('chat', __name__)

# Initialize components
embeddings = get_embeddings()
pc = initialize_pinecone(Config.PINECONE_API_KEY, Config.PINECONE_INDEX_NAME)
vector_store = get_vector_store(pc, Config.PINECONE_INDEX_NAME, embeddings)
llm = get_llm(Config.GEMINI_API_KEY)
retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 3})
qa_chain = create_qa_chain(llm, retriever)


@chat.route('/chat_page', methods=['GET'])
def chat_page():
    return render_template('chat.html')

@chat.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        question = data.get('question')
        
        if not question:
            return jsonify({'error': 'Question is required'}), 400
            
        response = qa_chain.invoke({"input": question})
        return jsonify({'answer': response['answer']})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500