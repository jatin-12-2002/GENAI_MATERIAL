from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


index_name="medical"

#Initializing the Pinecone
Pinecone(api_key=os.environ.get("PINECONE_API_KEY"),index_name=index_name)


#Creating Embeddings for Each of The Text Chunks & storing
docsearch=PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)