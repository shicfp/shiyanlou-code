# -*- coding:utf-8 -*-

'''
1. count the Q3, Q1 data through numpy or pandas
2. use if to judge
'''
import pandas as pd

def find_outlier(data): 
	''' receive a data file and return all the outliers'''

	outlier = []
	data_q = pd.Series(data).quantile([0.25, 0.5, 0.75])
	iqr = data_q.loc[0.75] - data_q.loc[0.25]

	for i in data:
		if i <= (data_q[0.25] - 1.5 * iqr) or i >= (data_q[0.75] + 1.5 * iqr):
			outlier.append(i)

	return outlier

list = [1, 2, 3, 5, 7, 8, 9, 12, 11, 10]
# pd.Series(list).describe()
print(find_outlier(list))