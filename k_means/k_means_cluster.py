#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy as np




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

exercised_stock_options_lst =[]
salary_lst =[]
for k, v in data_dict.iteritems():
    if v["exercised_stock_options"]!="NaN":
        exercised_stock_options_lst.append(float(v["exercised_stock_options"]))
    if v["salary"]!="NaN":
        salary_lst.append(float(v["salary"]))

print "Max of exercised_stock_options is", max(exercised_stock_options_lst), "and min is ", min(exercised_stock_options_lst)
print "Max of Salary is", max(salary_lst), "and min is ", min(salary_lst)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2,_ in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=0).fit(finance_features)
pred = kmeans.predict(finance_features)


from sklearn.preprocessing import MinMaxScaler

salary_lst.append(200000.0) #appending $200000.00 as salary to check the rescaled value
exercised_stock_options_lst.append(1000000.0)

salary_lst = np.array([[x] for x in salary_lst]) #converting into numpy array (array of array containing 1 feature)
exercised_stock_options_lst = np.array([[x] for x in exercised_stock_options_lst])

salary_scaler = MinMaxScaler()
stock_scaler = MinMaxScaler()

rescaled_salary = salary_scaler.fit_transform(salary_lst)
rescaled_exercised_stock = stock_scaler.fit_transform(exercised_stock_options_lst)

# printing the last values of each rescaled lists
print rescaled_salary[len(rescaled_salary)-1]
print rescaled_exercised_stock[len(rescaled_exercised_stock)-1]

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters_3_fet.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
