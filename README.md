# Immo Eliza - Model Deployment

## Learning Objectives

- Be able to deploy a machine learning model through an API endpoint
- Be able to deploy said API to Render 
- Be able to build a small web application using Streamlit

## The Mission

The real estate company Immo Eliza is really happy with your regression model and current work up to now.

They would like you to create an API so their web developers can access the predictions whenever they need to. They also want to have a small web application for the non-technical employees and possibly their clients to use. The API and the web application should be intertwined but separate.

  ## Data

- **Dataset**: Trained on 76 000 property listings in Belgium, focusing on houses and apartments.
- **Target**: To deploy a machine learning model through an API endpoint, Render and build a small web application using Streamlit
- **Features**: Includes bedrooms, property type, location, living area, garden/terrace presence, etc.

## Model Details

- **Chosen Model**: Random Forest was selected for its balance of performance and interpretability.
 Train Score: 0.89 – The model fits the training data well.
 Test Score: 0.68 – The model’s performance on unseen data is lower, indicating potential overfitting.


## Architecture

You will set up a:
- GitHub repository including your model artifacts
    - Option 1: the FastAPI code, the API Dockerfile, and a Render account to deploy your backend API
    - Option 2: Your streamlit code, and Streamlit Community Cloud account to deploy your frontend web application

    - Option 3: Combine the two. The below diagram summarizes the whole architecture.

    ![Architecture Diagram](architecture.png)


#### Input

An example input looks like:

```json
{
  "data": {
    "property_type": str,
    "region": str,
    "zip_code": int,
    "construction_year": int,
    "total_area_sqm": float,
    "nbr_bedrooms": int,
    "equipped_kitchen": Optional[Literal["INSTALLED", "HYPER_EQUIPPED", "NOT_INSTALLED","USA_UNINSTALLED","USA_HYPER_EQUIPPED","SEMI_EQUIPPED", 
                                         "USA_INSTALLED", "USA_SEMI_EQUIPPED"]] = None,
    "fl_furnished": Optional[bool],
    "fl_open_fire": Optional[bool],
    "terrace_sqm": Optional[float],
    "garden_sqm": Optional[float],
    "fl_swimming_pool": Optional[bool],
    "fl_floodzone": Optional[bool],
    "state_building": Optional[Literal["AS_NEW", "GOOD", "JUST_RENOVATED","TO_BE_DONE_UP","TO_RENOVATE","TO_RESTORE"]],
    "primary_energy_consumption_sqm": Optional[int],
    "heating_type": Optional[Literal["CARBON", "ELECTRIC", "FUELOIL","GAS","PELLET","SOLAR","WOOD"]],
    "fl_double_glazing": Optional[bool]

  }
}
```

#### Output

Your output should look like:

```json
{
  "prediction": Optional[float],
  "status_code": Optional[int]
}
```
## Steps

## 📦 Repo structure
```.
├── IMMO-ELIZA-DEPLOYMENT
│ └── immowebdeployment(env)
├  ── api 
├   │  ──app.py
├   │  ── Dockerfile
├   │  ── feature_names.pkl
├   │  ── model.pkl
├   │  ── predict.py
├   └  ── requirements.txt
├  ── streamlit
├    │ ── webapp.py    
├  ── .gitignore
├  ── README.md
 
```

### Prediction

In the previous project, you made a machine learning model to predict the price of a property. You stored its artifacts for both the preprocessing steps and the model.

The `predict.py` script will contain all the code to load your artifacts, preprocess your data, and generate a prediction.

The script should contain a `predict()` function that takes data for a single property (or possibly multiple properties) as an input and returns a price as output. The function should be a regular Python function, not a CLI tool.


### Option 1: Create your API

In your `app.py` file, create an API with FastAPI that contains two endpoints (also called routes):
- A route at `/` that accepts:
  - `GET` requests and returns `"alive"` if the server is up and running
- A route at `/predict` that accepts:
  - `POST` requests that receives the data of a property in JSON format and returns a prediction in JSON format

The function attached to your `/predict` endpoint should deal with all the input features provided as a JSON, preprocess them, pass them through your `predict()` function, and then return the prediction again as a JSON.

### 1.1 Create a Dockerfile for your API

The Dockerfile is a text file that contains all the commands to build an image and then run it as a container. Create a Dockerfile that runs your `app.py` file with Python.

```python
# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all contents from the api directory into /app in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r api/requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "api.app:immoapp", "--host", "0.0.0.0", "--port", "8000"]
```

 Deploy your Docker image on `render.com`

The hosting provider [Render](https://render.com/) allows you to build your Docker container on their server and send requests to it. 

### Streamlit application

Create a small web application using Streamlit that will allow non-technical people to use your API.

First we want to install Streamlit

```bash
# Install Streamlit
pip install streamlit

# Run the streamlit command
streamlit run streamlit/webapp.py

```

## ⏱️ Project Timeline
The initial setup of this project was completed in 6 days.

The project was completed as part of my 7-month AI training bootcamp at BeCode in Ghent, Belgium.




