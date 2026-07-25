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

theme = gr.themes.Soft(
    primary_hue="blue",
    neutral_hue="slate",
)

with gr.Blocks(
    title="Saint James Backpackers Assistant",
) as demo:

    gr.Markdown(
        """
<img class="logo" src="https://huggingface.co/spaces/SJ-1989/ChatSJB/resolve/main/Logo.png">

#### Hi, my name's Jack 👋
#### I'm your virtual assistant!
""",
        elem_id="intro",
    )

    gr.Markdown(
        """
I can help you with:

- 🛎️ Our services
- 📋 House rules
- 📍 Travel directions
""",
        elem_id="explanation",
    )

    question = gr.Textbox(
        label="Your Question",
        placeholder="What time is breakfast?",
        lines=1,
        render=False,
    )

    answer = gr.Markdown(
        label="Answer",
        elem_id="answer",
        render=False,
    )

    gr.Examples(
        examples=[
            "Do you have towels? 🚿",
            "When does the kitchen close? 🍴",
            "How do I get to Heathrow? ✈️"
        ],
        inputs=question,
        outputs=answer,
        fn=chatbot,
        cache_examples=False,
        run_on_click=True,
        label="Examples",
    )

    question.render()

    with gr.Row():
        ask_button = gr.Button("Ask", variant="primary")
        clear_button = gr.Button("Clear")

    answer.render()

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
    demo.launch(theme=theme, css=css)