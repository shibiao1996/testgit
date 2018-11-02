# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:17:27 2018

@author: biao
"""
import numpy as np

class LinearRegression:
    def __init__(self):
        ""初始化LinearRegression模型""
        self.coef_ = None
        self.interception_ = None
        self._theta = None
        
    def fit_normal(self,X_train, y_train):
        X_b = np.hstack([np.ones((len(X_train),1)),X_train])
        self._theta = np.linalg.inv(X_b,T,dot(X_b)).dot(X_b,T).dot(y_train);
        self.coef_ = self._theta[0]
        self.coef_ = self._theta[1:]
        
        return self
    
    def predict(self,X_predict):
        
        X_b = np.hstack([np.ones((len(X_predict),1)),X_predict])
        return X_b.dot(self,_theta)
    
    def score(self,X_test, y_test):
        return r2_score(y_test,y_predict)
        
    def __repr__(self):
        return "LinearRegression""