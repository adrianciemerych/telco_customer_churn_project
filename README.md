# This is a project about customers churn

## Introduction

A very important fact about customers in the companies is, that the keeping present customers is 6-7 times cheaper than obtaining a new customer. 
In this case a good move for the company is an observation of customers behaviour. 
This approach can lead to knowledge what is a reason of customers churn and enable special treatment for them.
Moreover, 5% budget increase on keeping customers can boost profits up to 95% received from regular clients.

## Dataset description

The dataset comprises 7043 customers of the company with 21 columns describing various features of each customer.

* customerID - customer ID
* gender - whether the customer is a male or a female
* SeniorCitizen - whether the customer is a senior citizen or not
* Partner - whether the customer has a partner or not
* Dependents - whether the customer has dependents or not
* tenure - number of months the customer has stayed with the company
* PhoneService - whether the customer has a phone service or not
* MultipleLines - whether the customer has multiple lines or not (Yes, No, No phone service)
* InternetService - customer’s internet service provider (DSL, Fiber optic, No)
* OnlineSecurity - whether the customer has online security or not (Yes, No, No internet service)
* OnlineBackup - whether the customer has online backup or not (Yes, No, No internet service)
* DeviceProtection - whether the customer has device protection or not (Yes, No, No internet service)
* TechSupport - whether the customer has tech support or not (Yes, No, No internet service)
* StreamingTV - whether the customer has streaming TV or not (Yes, No, No internet service)
* StreamingMovies - whether the customer has streaming movies or not (Yes, No, No internet service)
* Contract - the contract term of the customer (Month-to-month, One year, Two year)
* PaperlessBilling - whether the customer has paperless billing or not
* PaymentMethod - the customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
* MonthlyCharges - the amount charged to the customer monthly
* TotalCharges - the total amount charged to the customer
* Churn - whether the customer churned or not (target column)

## Main project - description

The main purpose of the project was to create a model that predict potential customer churn.
After proper preprocessing, selecting appriopriate features, the model was trained.
It has been taken into account that the dataset is imbalanced.
The more often the customers who could leave the company are more important.
It was included in a model also. Training the model with an f1 score (with beta = 2) 
provides the better focus on recall metric, that results higher number of correct predictions in terms of true churns

## Application - short description and tips

In the end of project model and standard scaler was saved to files. They are used in application to predict churn of customers.
Important thing is, the project was written with a version of sklearn = 1.2.2, so for correctly running application 
you must use the same version of this library. 
For start the application please type into the powershell command: streamlit run predict_churn_app.py


# Thanks for your time :)

