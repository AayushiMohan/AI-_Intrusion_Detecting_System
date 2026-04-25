import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model("ids_model.keras")

st.title("Intrusion Detection System")

st.write("Enter 41 feature values (comma separated)")

input_data = st.text_input("Input:")

if st.button("Predict"):
    try:
        data = [float(i) for i in input_data.split(",")]
        data = np.array(data).reshape(1, len(data), 1)

        pred = model.predict(data)

        if pred > 0.5:
            st.error("Attack Detected 🚨")
        else:
            st.success("Normal Traffic ✅")

    except:
        st.warning("Please enter valid input!")