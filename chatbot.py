import os
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity

from update_data import update_data

load_dotenv()

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_PAGE_ID = os.getenv('NOTION_PAGE_ID')
CHUNKS_USED = int(os.getenv('CHUNKS_USED'))

documents, tfidf_vectorizer, tfidf_matrix = update_data(NOTION_API_KEY, NOTION_PAGE_ID)

def chatbot(query: str) -> str:
    """
    Transforms the user query into tf-idf vectors and uses 
    cosine similarity to find the k best context chunks for
    an LLM to answer the question. 
    """
    query_vector = tfidf_vectorizer.transform([query])

    scores = cosine_similarity(query_vector, tfidf_matrix)[0]
    best = scores.argsort()[::-1][:CHUNKS_USED]

    best_k_chunks = [documents[num] for num in best]
    context = '\n\n'.join(best_k_chunks)

    return context