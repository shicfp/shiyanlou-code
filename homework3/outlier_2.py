# -*- coding:utf-8 -*-

'''
1. count the Q3, Q1 data through numpy or pandas
2. use if to judge
'''
import pandas as pd
import numpy as np

def find_outlier(data): 
	''' receive a data file and return all the outliers'''

	outlier = []
	array1 = np.array(data)
	q1 = np.percentile(array1, 25)
	q3 = np.percentile(array1, 75)
	iqr = q3 - q1
	behind = q1 - 1.5*iqr
	before = q3 + 1.5*iqr
	for i in data:
		if i < behind or i > before:
			outlier.append(i)

	return outlier


list = [1, 2, 3, 5, 7, 8, 9, 12, 11, 10, 100]
# pd.Series(list).describe()
print(find_outlier(list))