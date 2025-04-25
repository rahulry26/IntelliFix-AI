
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def search_logs(query_text):
    embeddings = OpenAIEmbeddings()
    db = Chroma(persist_directory="./intellifix_db", embedding_function=embeddings)
    results = db.similarity_search(query_text, k=2)
    for r in results:
        print(r.page_content)

search_logs("CrashLoopBackOff")

