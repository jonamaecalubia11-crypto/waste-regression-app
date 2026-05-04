import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

st.title("Smart Bin Prediction App")

# Input fields
weight_kg = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
item_count = st.number_input("Item Count", min_value=0, step=1)
avg_moisture = st.number_input("Average Moisture (%)", min_value=0.0, max_value=100.0, step=0.1)
days_since_collection = st.number_input("Days Since Collection", min_value=0, step=1)
bin_fill_percent = st.number_input("Current Bin Fill (%)", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Predict Bin Level"):
    input_data = pd.DataFrame([{
        "weight_kg": weight_kg,
        "item_count": item_count,
        "avg_moisture": avg_moisture,
        "days_since_collection": days_since_collection,
        "bin_fill_percent": bin_fill_percent
    }])

    # Align with model’s expected feature names
    input_data = input_data[model.feature_names_in_]

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Bin Fill Level: {prediction:.2f}%")
