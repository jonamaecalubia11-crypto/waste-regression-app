import streamlit as st
import numpy as np
import joblib

# Load model and polynomial transformer
model = joblib.load("model.pkl")
poly = joblib.load("poly.pkl")

# App title
st.title("♻️ Waste Bin Fill Level Predictor")

st.write("Enter the waste data below:")

# User Inputs
weight = st.number_input("Weight (kg)", min_value=0.0, value=1.0)
item_count = st.number_input("Item Count", min_value=0, value=1)
moisture = st.slider("Average Moisture (0 - 1)", 0.0, 1.0, 0.5)
days = st.number_input("Days Since Collection", min_value=0, value=1)

# Predict button
if st.button("Predict Fill Level"):
    try:
        # Prepare input (MUST be 2D and 4 features)
        input_data = np.array([[weight, item_count, moisture, days]])

        # Transform using PolynomialFeatures
        input_poly = poly.transform(input_data)

        # Predict
        prediction = model.predict(input_poly)[0]

        # Output result
        st.success(f"Predicted Fill Level: {prediction:.2f}%")

    except Exception as e:
        st.error(f"Error: {e}")
