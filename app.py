import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("♻️ Waste Bin Fill Predictor")

weight = st.number_input("Weight (kg)", min_value=0.0)
item_count = st.number_input("Item Count", min_value=0)
moisture = st.number_input("Average Moisture (0-1)", min_value=0.0, max_value=1.0)

def categorize(value):
    if value < 30:
        return "Empty"
    elif value < 70:
        return "Moderate"
    else:
        return "Full"

if st.button("Predict"):

    input_data = np.array([[weight, item_count, moisture]])

    st.write("Model expects:", model.n_features_in_)
    st.write("Input shape:", input_data.shape)

    try:
        prediction = model.predict(input_data)[0]
        prediction = max(0, min(100, prediction))

        def categorize(v):
            if v < 30:
                return "Empty"
            elif v < 70:
                return "Moderate"
            else:
                return "Full"

        st.success(f"Bin Status: {categorize(prediction)}")
        st.write(f"Predicted Fill Percent: {prediction:.2f}%")

    except Exception as e:
        st.error("Mismatch detected between model and input.")
        st.write(str(e))
