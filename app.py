import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

if st.button("Predict Bin Level"):

    input_data = pd.DataFrame([{
        "weight_kg": weight_kg,
        "item_count": item_count,
        "avg_moisture": avg_moisture,
        "days_since_collection": days_since_collection,
        "bin_fill_percent": bin_fill_percent
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Bin Level: {prediction:.2f}%")
    st.success(f"Predicted Bin Fill Level: {prediction:.2f}%")
