import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/model.pkl")

# App title
st.title("🔧 AI-Based Predictive Maintenance System")
st.write("Predict whether a machine is likely to fail.")

st.divider()

# Machine inputs
st.subheader("Machine Information")

product_type = st.selectbox(
    "Product Type",
    ["L", "M", "H"]
)

air_temperature = st.number_input(
    "Air Temperature [K]",
    min_value=250.0,
    max_value=350.0,
    value=300.0
)

process_temperature = st.number_input(
    "Process Temperature [K]",
    min_value=250.0,
    max_value=350.0,
    value=310.0
)

rotational_speed = st.number_input(
    "Rotational Speed [rpm]",
    min_value=500,
    max_value=3000,
    value=1500
)

torque = st.number_input(
    "Torque [Nm]",
    min_value=0.0,
    max_value=100.0,
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear [min]",
    min_value=0,
    max_value=300,
    value=100
)

# Prediction button
if st.button("🔍 Predict Machine Failure"):

    # Convert Product Type into model features
    type_L = 1 if product_type == "L" else 0
    type_M = 1 if product_type == "M" else 0

    # Create input dataframe
    input_data = pd.DataFrame({
        "Air temperature [K]": [air_temperature],
        "Process temperature [K]": [process_temperature],
        "Rotational speed [rpm]": [rotational_speed],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear],
        "Type_L": [type_L],
        "Type_M": [type_M]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.divider()

    if prediction == 1:
        st.error("⚠️ Possible Machine Failure")
        st.write("Maintenance should be considered.")
    else:
        st.success("✅ No Machine Failure Predicted")
        st.write("Machine is likely to operate normally.")
