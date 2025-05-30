extract_template = """
You are a strict information extractor. Extract customer data from the description below and return a **valid JSON object**.

- If a field is missing or unclear, return its value as **null**.
- Use these allowed values for categorical fields (or null if missing):
  - gender: "Male", "Female"
  - senior_citizen: "Yes", "No"
  - is_married: "Yes", "No"
  - dependents: "Yes", "No"
  - tenure: integer (in months)
  - phone_service: "Yes", "No"
  - dual: "Yes", "No", "No phone service"
  - internet_service: "DSL", "Fiber optic", "No"
  - online_security: "Yes", "No"
  - online_backup: "Yes", "No"
  - device_protection: "Yes", "No"
  - tech_support: "Yes", "No"
  - streaming_tv: "Yes", "No"
  - streaming_movies: "Yes", "No"
  - contract: "Month-to-month", "One year", "Two year"
  - paperless_billing: "Yes", "No"
  - payment_method: "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
  - monthly_charges: float
  - total_charges: float

Customer description:
{description}

Return only the JSON object with extracted fields.
"""

fill_missing_template = """
The previous extracted JSON had some missing fields with null values:

{json_data}

Please read the user's reply below carefully and extract values for **all missing fields** in a valid JSON object.

Use these allowed values for categorical fields (or null if missing):
  - gender: "Male", "Female"
  - senior_citizen: "Yes", "No"
  - is_married: "Yes", "No"
  - dependents: "Yes", "No"
  - tenure: integer (in months)
  - phone_service: "Yes", "No"
  - dual: "Yes", "No", "No phone service"
  - internet_service: "DSL", "Fiber optic", "No"
  - online_security: "Yes", "No"
  - online_backup: "Yes", "No"
  - device_protection: "Yes", "No"
  - tech_support: "Yes", "No"
  - streaming_tv: "Yes", "No"
  - streaming_movies: "Yes", "No"
  - contract: "Month-to-month", "One year", "Two year"
  - paperless_billing: "Yes", "No"
  - payment_method: "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
  - monthly_charges: float
  - total_charges: float

If a field is still missing or unclear, keep it as null.

Return only the JSON object containing these missing fields with extracted or null values.

User's reply:
{user_reply}
"""

response_template = """
You are a customer service expert.

Given these churn prediction results:

- Predicted Churn: {predicted_churn}
- Churn Probability: {churn_probability}%

Write a brief summary of what this means in plain language, followed by a short recommended action.  
Keep it concise and professional.
"""
