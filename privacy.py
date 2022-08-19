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
def identity_disclosure(real: DataFrame, synthetic: DataFrame):
    
    pass



def attribute_disclosure():
    pass