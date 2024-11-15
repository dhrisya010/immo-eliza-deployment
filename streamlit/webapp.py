import streamlit as st
import requests

# Define the API URL 
API_URL = "https://immo-eliza-deployment-yex3.onrender.com/predict"

# Define the Streamlit app title
st.title("🏠 ImmoWeb Price Prediction")

st.subheader("Enter Property Details:")

# Collect input fields
property_type = st.selectbox("🏢Property Type", ["Apartment", "House", "Studio", "Duplex"])
region = st.selectbox("🌍Region", ["Brussels", "Flanders", "Wallonia"])
zip_code = st.number_input("📍Zip Code", min_value=1000, max_value=9999, step=1)
construction_year = st.number_input("🛠️Construction Year", min_value=1800, max_value=2023, step=1)
total_area_sqm = st.number_input("📐Total Area (sqm)", min_value=10.0, max_value=1000.0, step=1.0)
nbr_bedrooms = st.number_input("🛏️Number of Bedrooms", min_value=0, max_value=10, step=1)

# Optional fields
equipped_kitchen = st.selectbox("🍽️Equipped Kitchen", ["INSTALLED", "HYPER_EQUIPPED", "NOT_INSTALLED","USA_UNINSTALLED","USA_HYPER_EQUIPPED","SEMI_EQUIPPED","USA_INSTALLED","USA_SEMI_EQUIPPED"])
furnished = st.checkbox("🛋️Furnished")
terrace_sqm = st.number_input("🌞Terrace Size (sqm)", min_value=0, max_value=1000, step=1)
garden_sqm = st.number_input("🌳Garden Size (sqm)", min_value=0, max_value=1000, step=1)
swimming_pool = st.checkbox("🏊 Swimming Pool")
state_building = st.selectbox("🏗️State of the Building", ["AS_NEW", "GOOD", "JUST_RENOVATED","TO_BE_DONE_UP","TO_RENOVATE","TO_RESTORE"])
primary_energy_consumption_sqm = st.number_input("⚡Energy Consumption (kWh/sqm)", min_value=0, max_value=1000, step=1)
heating_type = st.selectbox("🔥Heating Type", ["CARBON", "ELECTRIC", "FUELOIL","GAS","PELLET","SOLAR","WOOD"])
double_glazing = st.checkbox("🔲Double Glazing")

# Format the data for the API request
input_data = {
    "property_type": property_type,
    "region": region,
    "zip_code": int(zip_code),
    "construction_year": int(construction_year),
    "total_area_sqm": total_area_sqm,
    "nbr_bedrooms": int(nbr_bedrooms),
    "equipped_kitchen": equipped_kitchen,
    "fl_furnished": bool(furnished),
    "terrace_sqm": terrace_sqm if terrace_sqm > 0 else None,
    "garden_sqm": garden_sqm if garden_sqm > 0 else None,
    "fl_swimming_pool": swimming_pool,
    "state_building": state_building,
    "primary_energy_consumption_sqm": primary_energy_consumption_sqm if primary_energy_consumption_sqm > 0 else None,
    "heating_type": heating_type,
    "fl_double_glazing": double_glazing
}
# Make a prediction request to the API

if st.button("Predict Price"):
    with st.spinner("Predicting price..."):
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            predicted_price = response.json()["predicted_price"]
            st.markdown(f"""
                <div style="background-color:#f1f8e9; padding: 20px; border-radius: 10px; text-align: center;">
                    <h4 style="color:#388e3c;">Predicted Market Price</h4>
                    <p style="font-size: 28px; color:#388e3c; font-weight: bold;">€{predicted_price:,.2f}</p>
                    <p style="font-size: 16px; color:gray;">Based on the provided features, this is the estimated value of your property.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("🚨 An error occurred. Please check input values.")
