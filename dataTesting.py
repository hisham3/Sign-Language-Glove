import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support as score_collection
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt

file = pd.read_excel('glove.xlsx')
X = file.iloc[:, :4].values
y = file.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)

SVCModel = SVC(C=1, kernel='linear', gamma=1, shrinking=True)
SVCModel.fit(X_train, y_train)

predicted_svc = SVCModel.predict(X_test)

accuracy = accuracy_score(y_test, predicted_svc)

precision, recall, fscore, support = score_collection(y_test, predicted_svc)

con_matrix = confusion_matrix(y_test, predicted_svc)
plot_confusion_matrix(SVCModel, X_test, y_test)
plt.show()


