#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
for x, v in data_dict.iteritems():
    if v["salary"]!="NaN" and float(v["salary"])>1000000:
        print x, v["salary"],v["bonus"]
data_dict.pop("TOTAL",0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)




### your code below
salary_lst=[]

bonus_lst=[]
email_lst =[]
for point in data:
    # print point
    salary = point[0]
    bonus = point[1]
    salary_lst.append(salary)
    bonus_lst.append(bonus)
    matplotlib.pyplot.scatter( salary, bonus )
print "max salary", max(salary_lst)
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


