import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

class ServiceEngine:
    def __init__(self):
        self.llm = OpenAI(temperature=0.5, api_key=os.environ.get("OPENAI_API_KEY"))
        documents = SimpleDirectoryReader(input_files=["data/banking_faqs.txt"]).load_data()
        self.index = VectorStoreIndex.from_documents(documents)
        self.query_engine = self.index.as_query_engine()

    def handle_query(self, query):
        sanitized_query = query.replace('@', '').replace('user_id:', '')
        rag_result = self.query_engine.query(sanitized_query)
        prompt = PromptTemplate(input_variables=["context", "query"], template="Based on {context}, answer: {query}")
        full_prompt = prompt.format(context=rag_result, query=sanitized_query)
        return self.llm.invoke(full_prompt)