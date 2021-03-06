#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")

################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#######################################################################################################################
#######################################################################################################################
### K-nearest neighbor

# from sklearn.neighbors import KNeighborsClassifier
# perfect_k=3
# best_accuracy = 0.5
# # checking for perfect k with best accuracy
# for k in range(3, 199 , 2):
#     clf = KNeighborsClassifier(n_neighbors= k)
#     clf = clf.fit(features_train, labels_train)
#     pred = clf.predict(features_test)
#     accuracy = accuracy_score(pred, labels_test)
#     print "Using k as ",k , " accuracy = ", accuracy
#     if(accuracy> best_accuracy):
#         perfect_k = k
#         best_accuracy = accuracy
#
# ### accuracy = 0.936
# print "perfect k is ", perfect_k, " with accuracy of ", best_accuracy

#######################################################################################################################
#######################################################################################################################

#random forest algorithm
# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier(criterion='entropy', n_estimators=10)
# clf.fit(features_train, labels_train)
# # best accuracy = [0.932]   changeable

###################################################################################################################3###
#######################################################################################################################

#adaBoost

from sklearn.ensemble import AdaBoostClassifier

clf=AdaBoostClassifier()
clf.fit(features_train, labels_train)



pred = clf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print "accuracy = ", accuracy

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass



plt.show()