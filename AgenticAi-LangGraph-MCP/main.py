import sys

from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

sys.stdout.reconfigure(encoding="utf-8")

def main():
    print("Hello from agenticai-langgraph-mcp!")


if __name__ == "__main__":
    main()
    
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)
    store.load()
    # print(store.query("What is attention mechanism?", top_k=3))
    rag_search = RAGSearch()
    query = "Describe a simple home system with panels, inverter, optional battery, and grid connection."
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)