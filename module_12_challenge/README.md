# Module 12 Report

## Overview of the Analysis

The purpose of this analysis is to develop a machine learning model to predict outcomes of high risk loans. Credit risk poses a classification problem that’s inherently imbalanced. This is because healthy loans easily outnumber risky loans in credit risk loan populations. This project uses various techniques to train and evaluate models with imbalanced classes. 
The original dataset contains historical lending activity from a peer-to-peer lending services companies. Using this data we then use machine learning models to predict if a grouping of financial characteristics will result in a healthy or unhealthy loan.

The dataset consists of seven columns of borrowers financial history:
* Loan size
* Interest rate
* Borrower Income
* Debt to income 
* Number of accounts
* Derogatory marks
* Total debt

The target variable is loan status and contains a value of 1 when the loan is healthy and a 0 when the loan has a high risk of defaulting.


The loan status breakdown of the original data is:
* 75,036 loans labeled healthy (1)
* 2,500 loans labled unhealthy (0)


The following Machine Learning process were used:
* Split the data into training and testing datasets
* Created a Logistic Regression model (of categorical data) with the original data
* Fit the model to the testing data
* Evaluated the model using accuracy score, confusion matrix and a classification report. 
* Oversample the dataset then train model fit predict.
* Evaluate the model and compare metrics to determine which model is most effective for dataset.


## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  Balance Accuracy: 95%
  Precision:
      Healthy Loans - 1.00
      Unhealthy Loans - 0.85
  Recall:
      Healthy Loans - 0.99
      Unhealthy Loans - 0.91



* Machine Learning Model 2:
  Balance Accuracy: 99%
  Precision:
      Healthy Loans - 1.00
      Unhealthy Loans - 0.84
  Recall:
      Healthy Loans - 0.99
      Unhealthy Loans - 0.99
  

## Summary

In order to recommend a model it is necessary to indetify which metric is most critical then to optimize the model to that metric. With credit risk data being by nature an imbalanced class it is important to resample data using an oversampling techinique in order to increase the minority class to have more samples of test data for the model. 

A high accuracy score is not very relavent to our dataset since a high accuracy score merely reflects how many healthy loans exist in the original dataset. What is needed is to detemine if there is a higher cost associated with a false negative (recall metric) or a false positive (precision metric). With a false negative you will miss problems loans and score them as good loans thus increasing in error the total number of loans that are bound to default. With a false positive you simply mischaracterize good loans as ones likely to default. The latter has no risks of financial loss to the the lender. 

For this reason the second machine learning model using oversampled data with a higher recall score is the more useful model to determine which loans are most likely to default. Remember that the recall metric reveals how effectively a model correctly predicted the instances of a class versus the total number of instances that belong to that class. The second model increases recall by 8% and is better at identifying true unhealthy loans.




 




