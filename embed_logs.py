import openai
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os

# Set up your OpenAI API key
openai.api_key = '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'  # Replace with your actual OpenAI API key

def embed_log(log_text):
    # Convert log text into a Document object
    docs = [Document(page_content=log_text)]
    
    # Initialize embeddings using OpenAI
    embeddings = OpenAIEmbeddings()
    
    # Create the Chroma database from the document(s)
    db = Chroma.from_documents(docs, embeddings, persist_directory="./intellifix_db")
    
    # Persist the Chroma database
    db.persist()

# Example log text (you can replace it with your actual logs)
log_text = """
2025-04-25 10:00:00 INFO Starting IntelliFix AI engine...
2025-04-25 10:01:00 WARNING Database connection failed. Retrying...
2025-04-25 10:02:00 ERROR Unable to connect to the database after 3 retries.
"""

# Run the embedding function
embed_log(log_text)

