import gradio as gr
import requests
import json

SESSION_ID = "test"

def send_description(description, api_url):
    api_url = api_url.strip()
    if not api_url.endswith("/predict"):
        api_url = api_url.rstrip("/") + "/predict"

    payload = {
        "session_id": SESSION_ID,
        "description": description
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return f"Error: {e}", "", "", api_url

    status = data.get("status", "unknown")

    if status == "need_more_info":
        missing = data.get("missing_fields", {})
        if missing:
            missing_list = "\n".join(f"- {field}" for field in missing.keys())
            return f"There are some missing fields in the description.\n\nMissing fields:\n{missing_list}", "", "", api_url
        else:
            return f"Status: {status}\nNo missing fields info available.", "", "", api_url
    elif status == "success":
        explanation = data.get("explanation", "")
        features = data.get("data", {})
        pretty_features = json.dumps(features, indent=2)
        return explanation, pretty_features, "", api_url
    else:
        return str(data), "", "", api_url

with gr.Blocks(theme=gr.themes.Ocean()) as demo:
    gr.HTML("<style>textarea, .gr-box, .gr-button { font-size: 18px !important; }</style>")
    gr.HTML("<h2 style='font-size: 28px;'>Telecom Churn Prediction Chatbot</h2>")

    api_url_input = gr.Textbox(
        label="API Base URL (e.g. https://xxx.ngrok-free.app)",
        value="",
        lines=1
    )

    with gr.Row():
        with gr.Column(scale=2):
            description_input = gr.Textbox(
                label="Enter Customer Info",
                lines=6,
                placeholder="Type full description here..."
            )
            features_output = gr.Textbox(
                label="Parsed Features (JSON)", 
                lines=12, 
                interactive=False, 
                visible=True
            )
            send_btn = gr.Button("Send", variant="primary")
        with gr.Column(scale=3):
            output_text = gr.Textbox(label="Response", lines=15, interactive=False)

    send_btn.click(
        send_description,
        inputs=[description_input, api_url_input],
        outputs=[output_text, features_output, description_input, api_url_input]
    )

demo.launch()
