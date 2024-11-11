import pickle
import numpy as np
from train import testing_data
import pandas as pd


def predict_price(input_data):
    # Load model and feature names
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('feature_names.pkl', 'rb') as f:
        feature_names = pickle.load(f)
    
    # Convert input to DataFrame and one-hot encode
    input_df = pd.DataFrame([input_data])
    #input_df = pd.get_dummies(input_df)
    
    # Align input data with training feature names
    input_df = input_df.reindex(columns=feature_names, fill_value=0)
    
    # Predict and return the price
    predicted_price = model.predict(input_df)[0]    
    return predicted_price

    
# Example input data for a new house
input_data = {
                'property_type':'HOUSE',
                'region':'Flanders',
                'construction_year': 2010,
                'zip_code':'2100',
                 'nbr_bedrooms': 2,  
                 'total_area_sqm': 750,
                'terrace_sqm': 20  
             }
    
    # Predict the price
predicted_price = predict_price(input_data)
print(f"Predicted Price for the House: €{predicted_price}")









































