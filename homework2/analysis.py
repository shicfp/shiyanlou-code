import pandas as pd 
import json
import os

def analysis(file, user_id): 
	times = 0
	minutes = 0

	if os.path.exists(file): # 判断文件是否存在

		with open(file, 'r') as filedata:
			data_user = pd.read_json(filedata, orient = 'records') # 使用pd.read_json方法读取文件，并将文件保存为DataFrame数据类型，且columns即为json文件中的key值

			# 使用布尔表达式筛选出满足条件的数据，并分别count和sum；若值不存在，则会返回0
			times = data_user[data_user['user_id'] == user_id]['user_id'].count()
			minutes = data_user[data_user['user_id'] == user_id]['minutes'].sum()

	return times, minutes

print(analysis('a', 0)) # 测试