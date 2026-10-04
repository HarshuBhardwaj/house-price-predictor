import streamlit as st
import pandas as pd
import pickle
import os
# -----------------------------
# Load Model and Scaler
# -----------------------------



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "house_price_model.pkl"), "rb") as file:
    model = pickle.load(file)

with open(os.path.join(BASE_DIR, "scaler.pkl"), "rb") as file:
    scaler = pickle.load(file)


# -----------------------------
# Streamlit App
# -----------------------------

st.title("🏠 House Price Prediction")

st.write("Enter the details of the house to predict its price.")


# -----------------------------
# User Inputs
# -----------------------------

area = st.number_input(
    "Area (sq ft)",
    min_value=300,
    max_value=10000,
    value=2000
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=5,
    value=2
)

stories = st.number_input(
    "Number of Stories",
    min_value=1,
    max_value=5,
    value=2
)

parking = st.number_input(
    "Number of Parking Spaces",
    min_value=0,
    max_value=5,
    value=1
)


mainroad = st.selectbox(
    "Main Road Access",
    ["yes", "no"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["yes", "no"]
)

basement = st.selectbox(
    "Basement",
    ["yes", "no"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["yes", "no"]
)

prefarea = st.selectbox(
    "Preferred Area",
    ["yes", "no"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Price"):

    # Convert yes/no to 1/0
    mainroad = 1 if mainroad == "yes" else 0
    guestroom = 1 if guestroom == "yes" else 0
    basement = 1 if basement == "yes" else 0
    airconditioning = 1 if airconditioning == "yes" else 0
    prefarea = 1 if prefarea == "yes" else 0

    # Create input dataframe
    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus_semi-furnished": [
            1 if furnishingstatus == "semi-furnished" else 0
        ],
        "furnishingstatus_unfurnished": [
            1 if furnishingstatus == "unfurnished" else 0
        ]
    })


    # -----------------------------
    # Scale Numerical Features
    # -----------------------------

    numeric_cols = [
        "area",
        "bedrooms",
        "bathrooms",
        "stories",
        "parking"
    ]

    input_data[numeric_cols] = scaler.transform(
        input_data[numeric_cols]
    )


    # -----------------------------
    # Prediction
    # -----------------------------

    prediction = model.predict(input_data)[0]


    # -----------------------------
    # Display Result
    # -----------------------------

    st.success(
        f"🏠 Predicted House Price: ₹{prediction:,.0f}"
    )
