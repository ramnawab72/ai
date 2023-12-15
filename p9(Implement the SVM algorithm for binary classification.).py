import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

 
data = pd.read_csv('Iris.csv')

 
X = data.drop('Target', axis=1)
y = data['Target']

 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

 
svm_classifier = SVC(kernel='linear')  

 
svm_classifier.fit(X_train, y_train)

 
y_pred = svm_classifier.predict(X_test)

 
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
