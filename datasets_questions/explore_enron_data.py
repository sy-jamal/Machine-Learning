#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import itertools
import pickle


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "There are total ",len(enron_data), " people in the dataset"
print "There are ",len(enron_data[next(iter(enron_data))]), "Features of each person in the dataset"

count =0
for item in enron_data:
    if(enron_data[item]['poi']): count+=1

print "There are ",count,"person of interests"
print "James Prentice has $", enron_data["PRENTICE JAMES"]['total_stock_value'], " in stocks"
print "Wesley Colwell sent", enron_data["COLWELL WESLEY"]['from_this_person_to_poi'], " emails to POI"
print "Jeffrey K Skilling has exercised ", enron_data["SKILLING JEFFREY K"]['exercised_stock_options'], " stock options"

print "Jeffrey K Skilling took $",enron_data["SKILLING JEFFREY K"]['total_payments']
print "Kenneth Lay took $", enron_data["LAY KENNETH L"]['total_payments']
print "Andrew Fastow took $", enron_data["FASTOW ANDREW S"]['total_payments']

salary = list( v['salary'] for k,v in enron_data.items() if str(v['salary'])!='NaN')
print "There are total", len(salary), "salaries"

email_addresses = list( v['email_address'] for k,v in enron_data.items() if v['email_address']!='NaN')
print "There are total", len(email_addresses), "email addresses"

total_payment = list( v['total_payments'] for k,v in enron_data.items() if str(v['total_payments'])!='NaN')
print "There are total", len(total_payment), "payments"

total_poi_payment = list( v['total_payments'] for k,v in enron_data.items() if str(v['total_payments'])!='NaN' and v['poi'])
print "There are total", len(total_poi_payment), "payments for poi"