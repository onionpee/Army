from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

table = pd.read_csv("army.csv")     # pandas로 csv파일을 불러옴

label = table["rank"]       # 각 값에 열 값을 넣어줌
i = table["height"]
r = table["weight"]

wh = pd.concat([i, r], axis=1)

train_data, test_data, train_label, test_label = \
    train_test_split(wh, label, test_size=0.25, shuffle=True)

clf = svm.SVC()
clf.fit(train_data, train_label)

predict = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, predict)
print(ac_score)