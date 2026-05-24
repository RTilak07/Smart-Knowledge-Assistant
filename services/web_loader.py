from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document


def load_website(url):

    loader = WebBaseLoader(url)
    docs = loader.load()

    # Extract only website text
    full_text = "\n".join([doc.page_content for doc in docs])

    return [Document(page_content=full_text)]