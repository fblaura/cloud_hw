import pickle
import numpy as np
import json
import pandas as pd
# Load the trained model from current directory
with open('./output/Electrical_model.pkl', 'rb') as model_pkl:
    KRR_rbf = pickle.load(model_pkl)
if __name__ == "__main__":
    						
    new_record=np.array([[6.836982, 9.666273, 7.426696, 4.970267, 3.361971, -0.576022, -0.825520, -1.960429,0.160843,0.347951, 0.591763,0.106057]])
    predict_result = KRR_rbf.predict(new_record)
    print(predict_result)