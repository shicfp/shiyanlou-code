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


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# split data
X_train, X_test, y_train, y_test = train_test_split(
	feature, target, test_size=0.3, random_state=50)

# create model
model = RandomForestClassifier(random_state=10, n_estimators=10)

# train model
model.fit(X_train, y_train)

# predict
model.predict(X_test)

# test score
result = model.score(X_test, y_test)

print(result)


