# 🧪 Hospitality RAG Retrieval Eval
An evaluation testing retrieval strategies in a hospitality setting using a Chatbot connected to a Notion knowledge base. 

The experiment compares three retrieval strategies, TD-IDF, dense embeddings and a hybrid startegy (30/70 TF-IDF/dense embeddings). A Gradio-based chatbot connected to a Notion knowledge base is set up in a hostel in Kensington, London. That chatbot uses retrieval augmented generation (RAG), with text chunking based on document structure. After 300 questions are persisted to a Supabase database, a copy of the Notion knoweledge base is taken and persistence disabled. The questions are then encoded with the 'correct' text chunk(s) using LLM classification and human review. Finally, the three retrieval strategies are evaluated for accuracy using the real questions collected. 

**Key technologies:** Python, RAG, PostgreSQL, scikit-learn, SciPy, Google Gemini API, Jupyter.