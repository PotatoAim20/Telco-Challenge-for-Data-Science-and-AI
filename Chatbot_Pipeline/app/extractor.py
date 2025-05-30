from app.prompts import extract_template, response_template
import json, regex
from transformers import pipeline

# Loading HF pipeline
pipe = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.3",
    device=0,  # or -1 for CPU
    torch_dtype="auto",
    trust_remote_code=True
)

def extract_json(description):
    prompt_text = extract_template.format(description=description)
    output = pipe(prompt_text, max_new_tokens=512, do_sample=False)[0]['generated_text']
    generated_text = output[len(prompt_text):].strip()
    match = regex.search(r'\{(?:[^{}]|(?R))*\}', generated_text, regex.DOTALL)
    if not match:
        return None
    return json.loads(match.group())

def generate_churn_explanation(predicted_churn, churn_probability):
    prompt = response_template.format(
        predicted_churn=predicted_churn,
        churn_probability=f"{churn_probability:.2f}"
    )
    output = pipe(prompt, max_new_tokens=150, do_sample=False)[0]['generated_text']
    explanation = output[len(prompt):].strip()
    return explanation
