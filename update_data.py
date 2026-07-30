import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import spmatrix
from parse_notion_text import parse_notion_text


def get_notion_blocks(NOTION_API_KEY: str, NOTION_PAGE_ID: str) -> list[str]:
    """
    Sends a request to Notion to retrieve 'blocks' data from a page.
    Parses the data into chunks containing topic and text, finally 
     returning them combined as 'documents'. 
    """
    headers = {
            'Authorization': f'Bearer {NOTION_API_KEY}',
            'Notion-Version': '2022-06-28'
        }

    response = requests.get(
            f'https://api.notion.com/v1/blocks/{NOTION_PAGE_ID}/children',
            headers=headers
        )

    response.raise_for_status()

    chunks = parse_notion_text(response.json())

    documents = [
        f'Topic: {chunk["topic"]}\n\nText: {chunk["text"]}'
        for chunk in chunks
    ]

    return documents


def build_tfidf_matrix(documents: list[str]) -> tuple[TfidfVectorizer, spmatrix]:
    """
    Fits a TF-IDF vectorizer on the documents and returns the fitted
    vectorizer along with the TF-IDF document-term matrix.    
    """
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    return tfidf_vectorizer, tfidf_matrix


def update_data(
    NOTION_API_KEY: str,
    NOTION_PAGE_ID: str,
) -> tuple[list[str], TfidfVectorizer, spmatrix]:
    """
    Retrieves documents from Notion and creates a fitted TF-IDF vectorizer
    and matrix for document retrieval.
    """
    documents = get_notion_blocks(NOTION_API_KEY, NOTION_PAGE_ID)
    tfidf_vectorizer, tfidf_matrix = build_tfidf_matrix(documents)

    return documents, tfidf_vectorizer, tfidf_matrix






