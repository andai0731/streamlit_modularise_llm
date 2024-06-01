from elasticsearch import Elasticsearch
from langchain_community.embeddings import GooglePalmEmbeddings
# from langchain.llms import GooglePalm
from langchain_community.llms import GooglePalm
from pdf import get_pdf_chunks
from txt import get_txt_chunks
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain_elasticsearch import ElasticsearchStore
#import streamlit as st

embeddings = GooglePalmEmbeddings(google_api_key = API)

embedding = embeddings
elastic_vector_search = ElasticsearchStore(
    es_url="http://localhost:9200",
    index_name="test_index",
    embedding=embedding
)

doc_of_txt = get_txt_chunks("path to txt file")
doc_of_pdf = get_pdf_chunks("path to pdf file")
docs = doc_of_pdf + doc_of_txt

#embeddings = embeddings

db = ElasticsearchStore.from_documents(
    docs,
    embeddings,
    es_url="http://localhost:9200",
    index_name="test_index",
    strategy=ElasticsearchStore.ExactRetrievalStrategy(),
    
)

db.client.indices.refresh(index="test_index")

qa = RetrievalQA.from_chain_type(
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key="AIzaSyCmZ8bwEfRvdt_QXl45VF2NSZ2URfYFHPU", temperature=0.1),
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={'k': 1}),
    return_source_documents=True
)

def query_result(query):
	# qa = RetrievalQA.from_chain_type(
    # llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key="AIzaSyCmZ8bwEfRvdt_QXl45VF2NSZ2URfYFHPU", temperature=0.1),
    # chain_type="stuff",
    # retriever=db.as_retriever(search_kwargs={'k': 1}),
    # return_source_documents=True)
    result = qa({"query": query})
    answer = result["result"]
    #print(answer)
    return answer
