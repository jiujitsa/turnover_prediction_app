import uvicorn
from fastapi import FastAPI
from employee import Employee
import numpy as np
import pickle
import pandas as pd
import sklearn
# 2. Create the app object
app = FastAPI()
pickle_in = open("rf.pkl","rb")
rf=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
async def predict_turnover(info: Employee):

    info = info.dict()
    #info_array = np.array(list(info_dict.values()))
    #new_arr = info_array.reshape((1, -1))

    promoted=info["promoted"]
    review=info['review']
    projects=info['projects']
    tenure=info['tenure']
    satisfaction=info['satisfaction']
    bonus=info['bonus']
    avg_hrs_month=info['avg_hrs_month']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
   
    input_data = [[promoted, review, projects, tenure, satisfaction, bonus, avg_hrs_month]]

    prediction = rf.predict_proba([[promoted, review, projects, tenure, satisfaction, bonus, avg_hrs_month]]).tolist()[0]

    return {
        'prediction': prediction



    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7000)