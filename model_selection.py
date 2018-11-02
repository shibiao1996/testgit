# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:55:20 2018

@author: biao
"""
import numpy as np

def train_test_split(X,y,test_ratio=0.2,seed=None):
    
    assert X.shape[0] == y.shape[0],\
    "the size must be equal"
    assert 0.0 <= test_ratio <=1.0, \
    "test ratio must be valid"
    
    if seed:
        np.random.seed(seed)
        
        shuffled_indexes = np.random.permutation(len(X))
        
        test_size = int(len(X) * test_ratio)
        test_indexes = shuffled_indexes[:test_size]
        train_indexes = shuffled_indexes[test_size:]
        
        X_train = X[train_indexes]
        y_train = y[train_indexes]
        
        X_test = X[test_indexes]
        y_test = y[test_indexes]
    return (X_train, X_test, y_train, y_test)