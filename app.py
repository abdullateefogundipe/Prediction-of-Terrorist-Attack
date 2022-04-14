# -*- coding: utf-8 -*-
"""
Created on Tue April 11 21:40:41 2020
@author: limitless.ao
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from TerroristAttacks import TerroristAttack
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To ANN GROUP CAPSTONE PROJECT': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted terrorist attack successfulness
@app.post('/predict')
def predict_SuccessAttacks(data:TerroristAttack):
    data = data.dict()
    Year = data['Year']
    Month = data['Month']
    Day = data['Day']
    Extended = data['Extended']
    Country = data['Country']
    Region=data['Region']
    Suicide=data['Suicide']
    Attack_Type=data['Attack_Type']
    Target_Type=data['Target_Type']
    individual=data['individual']
    Nationality_target=data['Nationality_target']
    Attack_Group=data['Attack_Group']
    Weapon=data['Weapon']
    Number_of_Killed=data['Number_of_Killed']

  
   # print(classifier.predict([['Year', 'Month', 'Day', 'Extended', 'Country', 'Region', 'Suicide','Attack_Type', 'Target_Type',   'individual', 'Nationality_target', 'Attack_Group', 'Weapon', 'Number_of_Killed']]))
    prediction = classifier.predict([[Year, Month, Day, Extended, Country, Region, Suicide,Attack_Type, Target_Type, individual, Nationality_target, Attack_Group, Weapon, Number_of_Killed]])
    if(prediction[0]==1):
        prediction="Successful Terrorist Attack"
    else:
        prediction="Unsuccessful Terrorist Attack"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload