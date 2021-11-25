import json
import numpy as np
import os
import pickle
import joblib
import pandas as pd

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'Electrical_model.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    data=np.array(json.loads(raw_data)['data'])
    #inp=pd.DataFrame(data,index=[0])
    y_hat=model.predict(data)
    #y_hat = model.predict(inp)
    return json.dumps({"predicted:": float(y_hat)})