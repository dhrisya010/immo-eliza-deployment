from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Literal,Optional
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle


immoapp = FastAPI()


class ImmowebPricePrediction(BaseModel):
    # Required fields
    property_type: str
    region: str
    zip_code: int
    construction_year: int
    total_area_sqm: float
    nbr_bedrooms: int

    # Optional fields
    equipped_kitchen: Optional[Literal["INSTALLED", "HYPER_EQUIPPED", "NOT_INSTALLED","USA_UNINSTALLED","USA_HYPER_EQUIPPED","SEMI_EQUIPPED","USA_INSTALLED","USA_SEMI_EQUIPPED"]] = None
    fl_furnished: Optional[bool] = None
    terrace_sqm: Optional[float] = None
    garden_sqm: Optional[float] = None
    fl_swimming_pool: Optional[bool] = None
    state_building: Optional[Literal["AS_NEW", "GOOD", "JUST_RENOVATED","TO_BE_DONE_UP","TO_RENOVATE","TO_RESTORE"]] =None
    primary_energy_consumption_sqm: Optional[int] = None
    heating_type: Optional[Literal["CARBON", "ELECTRIC", "FUELOIL","GAS","PELLET","SOLAR","WOOD"]] = None
    fl_double_glazing: Optional[bool] = None


def preprocess_input(data: ImmowebPricePrediction):
    # Convert data to DataFrame (for consistency in encoding/scaling)
    input_data = pd.DataFrame([data.model_dump()])  # Use model_dump() instead of dict()

    # Process categorical features and one-hot encode them
    categorical_columns = ['property_type', 'region', 'equipped_kitchen', 'state_building', 'heating_type']
    input_data = pd.get_dummies(input_data, columns=categorical_columns)

    # Apply StandardScaler to the numerical features
    numeric_columns = ['zip_code', 'construction_year', 'total_area_sqm', 'nbr_bedrooms', 'terrace_sqm', 'garden_sqm', 'primary_energy_consumption_sqm']
    scaler = StandardScaler()
    input_data[numeric_columns] = scaler.fit_transform(input_data[numeric_columns])

    # Ensure the input data has the same features as the trained model by reordering
    with open('api/feature_names.pkl', 'rb') as f:
        feature_names = pickle.load(f)
    input_data = input_data.reindex(columns=feature_names, fill_value=0)

    return input_data
# get end point
@immoapp.get("/")
async def get():
    return {"message": "Alive"}

#POST end point
@immoapp.post("/predict")

async def predict(data: ImmowebPricePrediction):
    # Preprocess the incoming data
    processed_data = preprocess_input(data)

    # Load the trained model
    with open('api/model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Make prediction
    prediction = model.predict(processed_data)

    # Return the prediction result
    return {"predicted_price": prediction[0]}

