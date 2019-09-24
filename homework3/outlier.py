# -*- coding:utf-8 -*-

'''
解题思路：
1. count the Q3, Q1 data through numpy or pandas
需要统计Q3和Q1，自然想到利用pandas的统计特性进行处理，而指定数据类型为list，则最好使用series进行处理
2. use if to judge
使用if来做outlier的判断（思考：此处是否可以使用箱体图？）
'''
import pandas as pd

def find_outlier(data): 
	''' receive a data file and return all the outliers'''

	outlier = []
	data_q = pd.Series(data).quantile([0.25, 0.5, 0.75]) # 将文件data转化为series格式，并统计四分卫，
	iqr = data_q.loc[0.75] - data_q.loc[0.25]

	for i in data:
		if i <= (data_q[0.25] - 1.5 * iqr) or i >= (data_q[0.75] + 1.5 * iqr):
			outlier.append(i)

	return outlier

# 以下是测试时的用例
list = [1, 2, 3, 5, 7, 8, 9, 12, 11, 10]
# pd.Series(list).describe()
print(find_outlier(list))