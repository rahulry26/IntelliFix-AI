
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from parse_alert import parse_alert

def get_fix_recommendation(alert_text):
    embeddings = OpenAIEmbeddings()
    db = Chroma(persist_directory="./intellifix_db", embedding_function=embeddings)
    similar_logs = db.similarity_search(alert_text, k=3)
    context = "\n\n".join([doc.page_content for doc in similar_logs])

    llm = OpenAI(temperature=0.2)
    prompt = PromptTemplate(
        input_variables=["alert", "context"],
        template="""
        Given the alert:\n{alert}\n
        and past similar issues:\n{context}\n
        Suggest a fix or recovery step in a concise, actionable way.
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    fix = chain.run(alert=alert_text, context=context)
    return fix

alert = parse_alert("alerts/sample_alert.json")
fix = get_fix_recommendation(alert)
print("Suggested Fix:\n", fix)

