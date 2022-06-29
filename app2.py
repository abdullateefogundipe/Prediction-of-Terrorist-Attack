
#Import the required libraries for the machine learning application.

from numpy.core.numeric import True_
from sklearn import metrics
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score
import joblib

st.title('Streamlit WebApp For predicting Terrorist Attack')

    

def load():
    data= pd.read_csv("clean_df.csv")
    
    return data
df = load()

        
features = df[['Country', 'Region', 'Attack_Type', 'Target_Type', 'Attack_Group', 'Weapon', 'Suicide']]
target = df[['Success']]





cols = ['Country', 'Region', 'Attack_Type', 'Target_Type', 'Attack_Group', 'Weapon', 'Suicide']
st.sidebar.markdown(
            '<p class="header-style">Terrorist Attack Featutes</p>',
            unsafe_allow_html=True
        )
Country = st.sidebar.selectbox(
            f"Select {cols[0]}",
            sorted(features[cols[0]].unique())
        )

Region = st.sidebar.selectbox(
            f"Select {cols[1]}",
            sorted(features[cols[1]].unique())
        )

Attack_Type = st.sidebar.selectbox(
            f"Select {cols[2]}",
            sorted(features[cols[2]].unique())
        )
Target_Type = st.sidebar.selectbox(
            f"Select {cols[3]}",
                        sorted(features[cols[3]].unique())
        )
Attack_Group = st.sidebar.selectbox(
            f"Select {cols[4]}",
            sorted(features[cols[4]].unique())
        )

Weapon = st.sidebar.selectbox(
            f"Select {cols[5]}",
            sorted(features[cols[5]].unique())
        )
Suicide = st.sidebar.selectbox(
            f"Select {cols[6]}",
                        sorted(features[cols[6]].unique())
        )

#label encoding
label= LabelEncoder()


df['Country_n'] = label.fit_transform(df['Country'])
df['Region_n'] = label.fit_transform(df['Region'])
df['Attack_Type_n'] = label.fit_transform(df['Attack_Type'])
df['Target_Type_n'] = label.fit_transform(df['Target_Type'])
df['Attack_Group_n'] = label.fit_transform(df['Attack_Group'])
df['Weapon_n'] = label.fit_transform(df['Weapon'])

df = df.drop(['Country', 'Region', 'Attack_Type', 'Target_Type', 'Attack_Group', 'Weapon' ], axis='columns')
        
features = df[['Country_n', 'Region_n', 'Attack_Type_n', 'Target_Type_n', 'Attack_Group_n', 'Weapon_n', 'Suicide']]
target = df[['Success']]



# If button is pressed
if st.button("Submit"):

    # Unpickle classifier
    clf = joblib.load("classifier.pkl")

 #Store inputs into dataframe
    X = [Country, Region, Attack_Type, Target_Type, Attack_Group, Weapon, Suicide]
    X_n = label.fit_transform(X)
    X_n = np.array(X_n).reshape(1, -1)

    prediction = clf.predict(X_n)
    
    if prediction == 1:
        prediction=" a Successful Terrorist Attack"
    else:
        prediction=" an Unsuccessful Terrorist Attack"
   
    
    #Output prediction
    st.text(f"The model predicts  {prediction}")
  