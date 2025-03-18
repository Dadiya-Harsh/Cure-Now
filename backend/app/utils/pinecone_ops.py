from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

def initialize_pinecone(api_key, index_name):
    pc = Pinecone(api_key=api_key)
    return pc

def get_vector_store(pc, index_name, embeddings):
    return PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )