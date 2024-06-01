from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

def get_pdf_chunks(path):
    loader = PyMuPDFLoader(path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    docs = text_splitter.split_documents(documents)
    #print(docs[0])
    return docs


#get_pdf_chunks("/Users/vedant/Downloads/lang_chain_llm/Vedant_Dwivedi_2024.pdf")  

