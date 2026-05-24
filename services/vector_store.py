from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

VECTOR_PATH = "vector_store"


def create_vector_store(chunks):

        if not chunks:
            return None

        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        vector_db = FAISS.from_documents(chunks, embeddings)

        # Save vector database
        if not os.path.exists(VECTOR_PATH):
            os.makedirs(VECTOR_PATH)

        vector_db.save_local(VECTOR_PATH)

        return vector_db


def load_vector_store():

        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        if os.path.exists(VECTOR_PATH):

            return FAISS.load_local(
                VECTOR_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )

        return None    