#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    errors = pow((predictions - net_worths), 2)
    data = zip(ages, net_worths, errors)
    data.sort(key=lambda tup:tup[2])
    num_of_elem_needed = int(len(ages)*0.9)
    cleaned_data=data[:num_of_elem_needed]
    
    return cleaned_data

