import pandas as pd
import joblib

preprocessor = joblib.load("app/models/preprocessor_pipeline.joblib")
model = joblib.load("app/models/RandomForest_model.pkl")

def predict_churn(data):
    df = pd.DataFrame([data])
    processed = preprocessor.transform(df)
    pred = model.predict(processed)[0]
    prob = model.predict_proba(processed)[0][1]
    return pred, prob