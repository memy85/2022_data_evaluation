#%%
from pandas import Series, DataFrame
import pandas as pd
from numpy import array
import numpy as np

#%%
def compare_two_records(real : Series, synthetic : Series, distance):
    '''
    compares two give real and synthetic record
    metric -> hamming distance
    '''
    dist = sum(real == synthetic)
    
    if dist > distance : 
        return 0
    else :
        return 1
    

#%%
def identity_disclosure(real_1: DataFrame, real_2 : DataFrame, synthetic: DataFrame, hamming_distance = 5):
    '''
    real_1 : 합성에 사용된 원본 데이터
    real_2 : 합성에 사용되지 않은 원본 데이터
    synthetic : 합성된 데이터
    '''
    real1 = real_1.copy()
    real2 = real_2.copy()
    
    real1['category'] = 1
    real2['category'] = 2
    
    pd.concat([real1, real2])
    
    pass



def attribute_disclosure():
    pass