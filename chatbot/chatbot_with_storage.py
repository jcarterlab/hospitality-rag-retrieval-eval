import threading
import config
from chatbot.chatbot import chatbot
from database.save_query import save_query

def chatbot_with_storage(query: str, session_id: str,) -> str:
    """
    Generates a chatbot response and optionally stores the query.
    """
    response, response_type = chatbot(
        query,
        session_id,
    )

    if config.STORE_QUERIES:
        threading.Thread(
            target=save_query,
            kwargs={
                'query': query,
                'response_type': response_type,
                'chat_session_id': session_id,
            },
            daemon=True,
        ).start()

    return response
