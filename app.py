import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

st.title("Smart Waste Bin Level Predictor")

st.write("Enter bin data to predict fill level:")

bin_id = st.text_input("Bin ID (ignored or encoded if needed)")
weight_kg = st.number_input("Weight (kg)", min_value=0.0)
item_count = st.number_input("Item Count", min_value=0)
avg_moisture = st.slider("Average Moisture", 0.0, 1.0, 0.5)
days_since_collection = st.number_input("Days Since Collection", min_value=0)
bin_fill_percent = st.slider("Current Fill Estimate (optional)", 0, 100, 50)

if st.button("Predict Bin Level"):
    
    # IMPORTANT: match training feature order
    input_data = np.array([[
        weight_kg,
        item_count,
        avg_moisture,
        days_since_collection,
        bin_fill_percent
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Bin Fill Level: {prediction:.2f}%")
