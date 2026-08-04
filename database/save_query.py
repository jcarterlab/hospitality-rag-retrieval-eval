import logging
import config
from supabase import create_client

logger = logging.getLogger(__name__)

supabase = create_client(
    config.SUPABASE_URL,
    config.SUPABASE_KEY,
)

def save_query(
    query: str,
    response_type: str,
    chat_session_id: str | None = None,
):
    """
    Saves a user query and associated metadata to the Supabase database.
    """
    try:
        supabase.table('queries').insert({
            'query': query,
            'response_type': response_type,
            'chat_session_id': chat_session_id,
        }).execute()

    except Exception:
        logger.exception('Failed to save query')