from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor

import pandas as pd
import numpy as np

import pickle

## read the file

df=pd.read_csv(r'C:\Users\Sheikh Nabil\Anaconda\Desktop\capital-bike-share\flask app\final_18_19_20.csv')


## preprocess



df = df[['hour','holiday', 'weekday','count']]


df.holiday = df.holiday.astype('category')
df.weekday = df.weekday.astype('category')

df = pd.get_dummies(df)

## modelling

x = df.drop(columns = ['count'])
y = df['count']



ada = AdaBoostRegressor()
ada.fit(x,y)
pickle.dump(ada, open('model.pkl','wb'))
# line

