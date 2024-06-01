from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


def get_txt_chunks(path):
    loader = TextLoader(path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    docs = text_splitter.split_documents(documents)
    #print(docs[0])
    return docs

#get_txt_chunks("/Users/vedant/Downloads/lang_chain_llm/docker.txt")    
