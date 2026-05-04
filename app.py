import streamlit as st
import numpy as np
import joblib

# Load model + poly safely
model = joblib.load("model.pkl")
poly = joblib.load("poly.pkl")

st.title("♻️ Waste Bin Fill Predictor")

st.write("Enter waste bin data:")

weight = st.number_input("Weight (kg)", min_value=0.0)
item_count = st.number_input("Item Count", min_value=0)
moisture = st.number_input("Average Moisture (0-1)", min_value=0.0, max_value=1.0)
days = st.number_input("Days Since Collection", min_value=0)

def categorize(value):
    if value < 30:
        return "Empty"
    elif value < 70:
        return "Moderate"
    else:
        return "Full"

if st.button("Predict"):

    # IMPORTANT FIX: force correct shape + type
    input_data = np.array([[float(weight), float(item_count), float(moisture), float(days)]])

    try:
        # transform safely
        input_poly = poly.transform(input_data)

        # predict
        prediction = model.predict(input_poly)[0]

        # safety clamp (prevents weird values from breaking categories)
        prediction = max(0, min(100, prediction))

        category = categorize(prediction)

        st.success(f"Bin Status: {category}")
        st.write(f"Predicted Fill Percent: {prediction:.2f}%")

    except Exception as e:
        st.error("Prediction failed due to model mismatch.")
        st.write("Error details:", str(e))
        st.stop()
