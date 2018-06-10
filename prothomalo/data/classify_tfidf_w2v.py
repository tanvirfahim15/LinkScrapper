import numpy as np
from sklearn.cross_validation import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


df = pd.read_csv('trainset_tfidf_w2v.csv',sep=',', header=None)
arr = np.array(df)
y = arr[:, 0]
X = arr[:, 1:]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

logisticRegr = LogisticRegression()
logisticRegr.fit(X_train, y_train)
predict_test = logisticRegr.predict(X_test)
error_count = 0
error_set = {}
for i in range(y_test.__len__()):
	if predict_test[i] != y_test[i]:
		error_count = error_count+1
	if y_test[i] not in error_set:
		error_set[y_test[i]]=1
	else:
		error_set[y_test[i]] = error_set[y_test[i]]+1

print('Accuracy:'+str((1-(error_count/y_test.__len__()))*100)+'%')
print('Error:'+str(error_count/y_test.__len__()*100)+'%')
print()


print(classification_report(y_test, predict_test))

