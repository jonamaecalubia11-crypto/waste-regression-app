import streamlit as st

st.title("Waste Bin Input App")

st.write("Enter bin data below:")

bin_id = st.text_input("Bin ID")
weight_kg = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
item_count = st.number_input("Item Count", min_value=0)
avg_moisture = st.slider("Average Moisture", 0.0, 1.0, 0.5)
days_since_collection = st.number_input("Days Since Collection", min_value=0)
bin_fill_percent = st.slider("Bin Fill Percent", 0, 100, 50)

if st.button("Submit"):
    st.write("### Collected Input Data")
    st.write({
        "bin_id": bin_id,
        "weight_kg": weight_kg,
        "item_count": item_count,
        "avg_moisture": avg_moisture,
        "days_since_collection": days_since_collection,
        "bin_fill_percent": bin_fill_percent
    })
