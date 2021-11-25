from sklearn.model_selection import train_test_split
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_poisson_deviance
################# metricas
from sklearn.metrics import explained_variance_score   
from sklearn.metrics import mean_absolute_error 
import pandas as pd
import numpy as np
import pickle 
#from azure.core import Run 
#run = Run.get_context()
#descarga dataset
dataset="https://raw.githubusercontent.com/fblaura/cloud_hw/main/Electrical.csv"
df=pd.read_csv(dataset)

x = df[['tau1','tau2','tau3','tau4','p1','p2','p3','p4','g1','g2','g3','g4']]
y = df['stab'] 

#train and test

X_train,X_test,y_train,y_test = train_test_split(x,y, test_size = 0.2, random_state = 17)

KRR_rbf = KernelRidge(alpha = 1, gamma = 0.1, kernel = 'rbf') # Utilizando un kernel de base radial (Gaussiana)
KRR_rbf.fit(X_train.values, y_train)
y_pred = KRR_rbf.predict(X_test.values)

#métricas
Puntaje_1 = explained_variance_score(y_test, y_test) 
print("Varianza Explicada = {:.4f}".format(Puntaje_1))

Puntaje_2 = mean_absolute_error(y_test, y_pred)
print("MAE = {:.4f}".format(Puntaje_2))

#run.log('accuracy', scores[0])
Pkl_Filename = "output\Electrical_model.pkl"
#Registro modelo

with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(KRR_rbf, file)
