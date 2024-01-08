import streamlit as st
import pickle
import pandas as pd

# This is a simple web application for making predictions about customers churn.
# Adding informations about customer on local host and clicking 'predict' button,
# we can simply predict if customer will leave the company or not (with some probability)

# Writing a title text
st.write('# Application for predicting customers churn')

# Creating columns
col1, col2 = st.columns(2)

# Adding cells with inputs
totalCharges = col1.number_input('Enter Total Charges')
tenure = col2.number_input('Enter tenure')
monthlyCharges = col1.number_input('Enter monthly charges')
contract = col2.selectbox('Enter type of contract', ['Month-to-month', 'One year', 'Two year'])
partner = col1.selectbox('Has a partner?', ['Yes', 'No'])
dependents = col2.selectbox('Has dependents?', ['Yes', 'No'])
seniorCitizen = col1.selectbox('Senior citizen?', ['Yes', 'No'])
paymentMethod = col2.selectbox('Enter a payment method', ['Electronic check', 'Mailed check',
                                                          'Bank transfer (automatic)', 'Credit card (automatic)'])
paperlessBilling = col1.selectbox('Paperless billing?', ['Yes', 'No'])
internetService = col2.selectbox('Enter type of internet service', ['No internet service', 'Fiber optic', 'DSL'])

if internetService != 'No internet service':
    onlineSecurity = col1.selectbox('Has an online security?', ['Yes', 'No'])
    techSupport = col2.selectbox('Has a tech support?', ['Yes', 'No'])
    onlineBackup = col1.selectbox('Has an online backup?', ['Yes', 'No'])
    deviceProtection = col2.selectbox('Has a device protection?', ['Yes', 'No'])
    streamingMovies = col1.selectbox('Has a streaming movies?', ['Yes', 'No'])
    streamingTV = col2.selectbox('Has a streaming TV?', ['Yes', 'No'])
else:
    onlineSecurity, techSupport, onlineBackup, deviceProtection, streamingMovies, streamingTV = 6*['No internet service']

# Creating a dataframe with columns ordered like in random forest classifier
df = pd.DataFrame(columns = ['TotalCharges', 'tenure', 'MonthlyCharges', 'Contract_Two year',
                             'InternetService_Fiber optic', 'PaymentMethod_Electronic check', 'Contract_One year',
                             'OnlineSecurity_Yes',	'TechSupport_Yes', 'PaperlessBilling_Yes', 'Partner_Yes',
                             'OnlineBackup_Yes', 'Dependents_Yes', 'SeniorCitizen_1', 'DeviceProtection_Yes',
                             'StreamingMovies_Yes', 'StreamingTV_Yes', 'PaymentMethod_Credit card (automatic)',
                             'tenure_cats_3-70', 'PaymentMethod_Mailed check', 'StreamingTV_No internet service'])

# Converting category columns to 1 and 0, which are necessary for prediction
contractTwoYear = 1 if contract == 'Two year' else 0
internetServiceFiberOptic = 1 if internetService == 'Fiber optic' else 0
paymentMethodElectronicCheck = 1 if paymentMethod == 'Electronic check' else 0
contractOneYear = 1 if contract == 'One year' else 0
onlineSecurity_yes = 1 if onlineSecurity == 'Yes' else 0
techSupport_yes = 1 if techSupport == 'Yes' else 0
paperlessBilling_yes = 1 if paperlessBilling == 'Yes' else 0
partner_yes = 1 if partner == 'Yes' else 0
onlineBackup_yes = 1 if onlineBackup == 'Yes' else 0
dependents_yes = 1 if dependents == 'Yes' else 0
seniorCitizen_yes = 1 if seniorCitizen == 'Yes' else 0
deviceProtection_yes = 1 if deviceProtection == 'Yes' else 0
streamingMovies_yes = 1 if streamingMovies == 'Yes' else 0
streamingTV_yes = 1 if streamingTV == 'Yes' else 0
paymentMethodCreditCard = 1 if paymentMethod == 'Credit card (automatic)' else 0
tenureThreeSeventyCat = 1 if (tenure > 3 and tenure <= 70) else 0
paymentMethodMailedCheck = 1 if paymentMethod == 'Mailed check' else 0
streamingTVNoInternetService = 1 if streamingTV == 'No internet service' else 0

# Adding values to dataframe
df.loc[0] = [totalCharges, tenure, monthlyCharges, contractTwoYear, internetServiceFiberOptic,
             paymentMethodElectronicCheck, contractOneYear, onlineSecurity_yes, techSupport_yes,
             paperlessBilling_yes, partner_yes, onlineBackup_yes, dependents_yes, seniorCitizen_yes,
             deviceProtection_yes, streamingMovies_yes, streamingTV_yes, paymentMethodCreditCard,
             tenureThreeSeventyCat, paymentMethodMailedCheck, streamingTVNoInternetService]

# Loading pickle files - Standard Scaler and Random Forest Classifier
with open('predict_churn_scaler.pickle', 'rb') as f:
    scaler = pickle.load(f)

with open('predict_churn_random_forest_classifier.pickle', 'rb') as f:
    randomForestClassifier = pickle.load(f)

# Transforming the data using StandardScaler fitted on training set
df[['tenure', 'MonthlyCharges', 'TotalCharges']] = scaler.transform(df[['tenure', 'MonthlyCharges', 'TotalCharges']])

# Making prediction of passed data and calculating probability of churn
prediction = randomForestClassifier.predict(df)
probability = round(randomForestClassifier.predict_proba(df)[0][1]*100, 2)

# Creating a button which will be showing the result of prediction
if st.button('Predict'):
    if(prediction[0] == 0):
        st.write('<p class="big-font">This customer probably will stay with the company.</p>', unsafe_allow_html=True)
    else:
        st.write(f'<p class="big-font">There is a high likelihood for the customer churn and it is equal to  {probability}%</p>',
                 unsafe_allow_html=True)

