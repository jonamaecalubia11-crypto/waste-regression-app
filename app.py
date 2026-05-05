import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")
poly = joblib.load("poly.pkl")

# Categorization function
def categorize(value):
    if value < 30:
        return "Empty"
    elif value < 70:
        return "Moderate"
    else:
        return "Full"

# UI
st.title("♻️ Waste Bin Fill Level Predictor")

weight = st.number_input("Weight (kg)", min_value=0.0, value=1.0)
item_count = st.number_input("Item Count", min_value=0, value=1)
moisture = st.slider("Average Moisture (0 - 1)", 0.0, 1.0, 0.5)
days = st.number_input("Days Since Collection", min_value=0, value=1)

if st.button("Predict"):
    try:
        input_data = np.array([[weight, item_count, moisture, days]])
        input_poly = poly.transform(input_data)
        prediction = model.predict(input_poly)[0]

        category = categorize(prediction)

        # Display results
        st.success(f"Predicted Fill Level: {prediction:.2f}%")
        st.info(f"Bin Status: {category}")

        # Optional visual
        st.progress(min(int(prediction), 100))

    except Exception as e:
        st.error(f"Error: {e}")
