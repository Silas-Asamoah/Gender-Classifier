from sklearn import tree 
from sklearn.svm import SVC 
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np 

 #[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#Classifiers
clf_tree = tree.DecisionTreeClassifier()
clf_svm = SVC()
clf_perceptron = Perceptron()
clf_knc = KNeighborsClassifier()

#Training the models
clf_tree.fit(X, Y)
clf_svm.fit(X, Y)
clf_perceptron.fit(X, Y)
clf_knc.fit(X, Y)

#Testing using the same data
pred_tree = clf_tree.predict(X)
acc_tree = accuracy_score(Y, pred_tree) * 100
print("Accuracy for DecisionTree: {}".format(acc_tree))

pred_svm = clf_svm.predict(X)
acc_svm = accuracy_score(Y, pred_svm) * 100
print("Accuracy for SVM: {}".format(acc_svm))

pred_per = clf_perceptron.predict(X)
acc_per = accuracy_score(Y, pred_per) * 100
print("Accuracy for Perceptron: {}".format(acc_per))

pred_knc = clf_knc.predict(X)
acc_knc = accuracy_score(Y, pred_knc) * 100
print("Accuracy for KNN: {}".format(acc_knc))

#The best classifier from Support Vector Machines(SVM), Perceptron and KNeighborsClassifier
index = np.argmax([acc_svm, acc_per, acc_knc])
classifiers = {0: "SVM", 1: "Perceptron", 2: "KNN"}
print("Best gender classifier is {}".format(classifiers[index]))
