from fastapi import FastAPI
import uvicorn
import pickle
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel
from sklearn.ensemble import RandomForestRegressor

app = FastAPI()

#Load the model
model = pickle.load(open('../models/final_model.pkl', 'rb'))
    
#Load preprocessor
country_encoder = joblib.load(open('../models/encoded_country.pkl', 'rb'))

if isinstance(country_encoder, pd.Series):
    global_mean = country_encoder.mean()
else:
    global_mean = np.mean(list(country_encoder.values()))

class InputData(BaseModel):
    year: int
    adult_mortality: float
    alcohol: float
    hepatitis_b: float
    measles: int
    bmi: float
    under_five_deaths: int
    polio: float
    total_expenditures: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    schooling: float
    thinness: float
    country: str
    
    

@app.post("/predict")
def predict(data: InputData):
    encoded_country = country_encoder.get(data.country, global_mean)
    
    X =np.array([[data.year, data.adult_mortality, data.alcohol, data.hepatitis_b,
                      data.measles, data.bmi, data.under_five_deaths, data.polio,
                      data.total_expenditures, data.diphtheria, data.hiv_aids,
                      data.gdp, data.schooling, data.thinness, encoded_country]])
    y_pred = model.predict(X)[0]
    
    return {"life_expectancy": y_pred[0]}

if __name__ == "__main__":
    uvicorn.run(app)