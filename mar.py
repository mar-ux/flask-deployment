# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:06:32 2021

@author: smai212
"""

import numpy as np
import pandas as pd
import pickle
df=pd.read_csv('hiring.csv')  
df['test_score(out of 10)'].fillna(df['test_score(out of 10)'].median(),inplace=True)
df['experience'].fillna(0,inplace=  True)
def word_to_dict(word):
    dict={0:0,'zero':0,'one':1,'four':4,'six':6,'eight':8,'five':5,"two":2,
          'seven':7,'three':3,'ten':10,'eleven':11}
    return dict[word] 
df['experience']=df['experience'].apply(lambda x:word_to_dict(x))
x=df.iloc[:,0:3]
y=df.iloc[:,-1]
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x,y)
pickle.dump(lr,open('marmodel.pkl','wb'))
marmodel=pickle.load(open('marmodel.pkl','rb'))
print(marmodel.predict([[2,9,6]]))