
import streamlit as st
import requests



# Define the API URL (replace with your deployed URL on Render)
API_URL = "https://your-app-name.onrender.com/predict"

# Streamlit UI
st.set_page_config(page_title="Real Estate Price Prediction", layout="centered")
st.title("🏠 Real Estate Price Prediction")
st.write("Fill in the property details below to get an estimated price.")

# Use columns for layout organization
col1, col2 = st.columns(2)

with col1:
    property_type = st.selectbox("🏢 Property Type", ["Apartment", "House", "Studio", "Duplex"])
    region = st.selectbox("🌈🌈🌈 Region", ["Brussels", "Flanders", "Wallonia"])
    zip_code = st.number_input("📍 Zip Code", min_value=1000, max_value=9999, step=1)
    construction_year = st.number_input("🛠️ Construction Year", min_value=1800, max_value=2023, step=1)
    total_area_sqm = st.number_input("📐 Total Area (sqm)", min_value=10.0, max_value=1000.0, step=1.0)
    nbr_bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=0, max_value=10, step=1)





# Format the data for the API request
input_data = {
    "property_type": property_type,
    "region": region,
    "zip_code": int(zip_code),
    "construction_year": int(construction_year),
    "total_area_sqm": total_area_sqm,
    "nbr_bedrooms": int(nbr_bedrooms),
   
}

# Prediction request
if st.button("Predict Price"):
    with st.spinner("Predicting price..."):
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            predicted_price = response.json()["predicted_price"]
            st.success(f"The predicted price is: €{predicted_price:,.2f}")
        else:
            st.error("An error occurred. Please check input values.")
