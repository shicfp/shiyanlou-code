# -*- coding:utf-8 -*-

import pandas as pd 

data = pd.read_csv("credit_card_train.csv", header=0) # ????

# deal with data
data1 = pd.get_dummies(data[['SEX', 'EDUCATION', 'MARRIAGE']])
data2 = data.iloc[:, 0: 14]
data3 = data.DEFAULT
data = data2.join(data1)
data = data.join(data3)


# define feature and target
feature = data.iloc[:, 1:-1].values
target = data['DEFAULT'].values

# split data
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
X_train, X_test, y_train, y_test = train_test_split(
	feature, target, test_size=0.3, random_state=50)

# create model
model = DecisionTreeClassifier()

# train model
model.fit(X_train, y_train)

# predict
model.predict(X_test)

# test score
result = model.score(X_test, y_test)

print(result)

# ClassCode = pd.DataFrame([1, 0], index=['Yes', 'NO'], columns=['ClassCode']) # repalce yes&no to 0/1
# data = data.join(ClassCode, how='left', on=data.DEFAULT)
# data = data.drop(['DEFAULT'], axis=1)