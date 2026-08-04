import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_PAGE_ID = os.getenv('NOTION_PAGE_ID')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = os.getenv('MODEL')

CHUNKS_USED = int(os.getenv('CHUNKS_USED', 3))
USE_AI = os.getenv('USE_AI', 'false').lower() == 'true'
RETRIEVAL_METHOD = os.getenv('RETRIEVAL_METHOD', 'tfidf') # tfidf, dense_embeddings, hybrid
TFIDF_WEIGHT = float(os.getenv('TFIDF_WEIGHT', 0.3))
DENSE_EMBEDDINGS_WEIGHT = float(os.getenv('TFIDF_WEIGHT', 0.7))

STORE_QUERIES = os.getenv('STORE_QUERIES', 'false').lower() == 'true'
SUPABASE_URL = os.getenv('SUPABASE_URL', '')
SUPABASE_KEY = os.getenv('SUPABASE_KEY', '')