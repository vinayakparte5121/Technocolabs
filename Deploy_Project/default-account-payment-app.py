import streamlit as st
import pandas as pd
import pickle

import warnings
warnings.filterwarnings('ignore')

## Header line for the app
st.write("""
	# Default Payment Prediction App  !! """)

st.subheader('Developed by : Vinayak Parte')
##Header for the side bar
st.sidebar.header("Please enter your parameters")

##Creating a function to take all the input values from the web page 
def user_input_features():
    LIMIT_BAL = st.sidebar.slider("LIMIT_BAL",0,800000,1000)
    #EDUCATION = st.sidebar.slider("EDUCATION",0,2)
    EDUCATION = st.sidebar.selectbox('EDUCATION',(1, 2, 3))
    MARRIAGE = st.sidebar.selectbox('MARRIAGE',(1, 2, 3))
    AGE = st.sidebar.slider("AGE",21,80)
    PAY_1 = st.sidebar.slider("PAY_1",0,10000)
    BILL_AMT1= st.sidebar.slider("BILL_AMT1",0,10000)
    BILL_AMT2= st.sidebar.slider("BILL_AMT2",0,10000)
    BILL_AMT3= st.sidebar.slider("BILL_AMT3",0,10000)
    BILL_AMT4= st.sidebar.slider("BILL_AMT4",0,10000)
    BILL_AMT5= st.sidebar.slider("BILL_AMT5",0,10000)
    BILL_AMT6= st.sidebar.slider("BILL_AMT6",0,10000)
    PAY_AMT1 = st.sidebar.slider("PAY_AMT1",0,10000)
    PAY_AMT2 = st.sidebar.slider("PAY_AMT2",0,10000)
    PAY_AMT3 = st.sidebar.slider("PAY_AMT3",0,10000)
    PAY_AMT4 = st.sidebar.slider("PAY_AMT4",0,10000)
    PAY_AMT5 = st.sidebar.slider("PAY_AMT5",0,10000)
    PAY_AMT6 = st.sidebar.slider("PAY_AMT6",0,10000)
    

	#creating dictionary for the input parameters
    data = {"LIMIT_BAL":LIMIT_BAL,"EDUCATION":EDUCATION,"MARRIAGE":MARRIAGE,"AGE":AGE,"PAY_1":PAY_1,
            "BILL_AMT1":BILL_AMT1,"BILL_AMT2":BILL_AMT2,"BILL_AMT3": BILL_AMT3,'BILL_AMT4':BILL_AMT4,'BILL_AMT5':BILL_AMT5,
            'BILL_AMT6':BILL_AMT6,'PAY_AMT1':PAY_AMT1,'PAY_AMT2':PAY_AMT2,
            'PAY_AMT3':PAY_AMT3,'PAY_AMT4':PAY_AMT4,'PAY_AMT5':PAY_AMT5,
            'PAY_AMT6':PAY_AMT6}

	#converting the dictionary to dataframe 
    features = pd.DataFrame(data,index=[0])
    return features

## Calling the above function 
df = user_input_features()

#loading the model 
lr_model = pickle.load(open('rfc.pkl','rb'))

## Predicting the inputs from the user 
prediction = lr_model.predict(df)


##Printing the prediction on web page
st.subheader("Prediction")

if prediction == 0 :
    st.write('There are **low** chances of the account getting default next month.')
else:
    st.write('There are **high** chances of the account getting default next month.')


