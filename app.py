from pathlib import Path
import gradio as gr
from chatbot import chatbot

# -------------------------
# CSS styles
# -------------------------

css = Path("styles.css").read_text()

# -------------------------
# Gradio UI
# -------------------------

with gr.Blocks(
    title="Saint James Backpackers Assistant",
    theme=gr.themes.Soft(),
    css=css,
) as demo:

    gr.Markdown(
        """
# 🎒 ChatSJB

### Saint James Backpackers' Assistant
""",
        elem_id="intro",
    )

    gr.Markdown(
        """
Welcome!

Ask me something about your stay.

I can help with:

- 🛎️ What we offer
- 📋 Hostel policies
- 📍 Travel directions

""",
        elem_id="explanation",
    )

    question = gr.Textbox(
        label="Your Question",
        placeholder="What time is breakfast?",
        lines=1,
    )

    with gr.Row():
        ask_button = gr.Button("Ask", variant="primary")
        clear_button = gr.Button("Clear")

    answer = gr.Markdown(
        label="Answer",
        elem_id="answer",
    )

    ask_button.click(
        fn=chatbot,
        inputs=question,
        outputs=answer,
    )

    question.submit(
        fn=chatbot,
        inputs=question,
        outputs=answer,
    )

    clear_button.click(
        lambda: ("", ""),
        outputs=[question, answer],
    )

# -------------------------
# Entry point
# -------------------------

if __name__ == "__main__":
    demo.launch()