import streamlit as st
import pandas as pd
import joblib


# Title
st.header("PREDICTION OF SUCCESSFUL TERRORIST ATTACK")

# Input bar 1
Year = st.number_input("Enter Year [1970 - 2017]")

# Input bar 2
Month = st.number_input("Enter Month [1-12]")

# Input bar 3
Day = st.number_input("Enter Day")

# Input bar 4
Extended = st.number_input("Enter Extended [0-1]")

# Input bar 5
Country = st.number_input("Enter Country")

# Input bar 6
Region = st.number_input("Enter Region")

# Input bar 7
Suicide = st.number_input("Enter Suicide")

# Input bar 8
Attack_Type = st.number_input("Enter Attack_Type")

# Input bar 9
Target_Type = st.number_input("Target_Type")

# Input bar 10
individual = st.number_input("Enter individual")


# Input bar 11
Nationality_target = st.number_input("Enter Nationality_target")

# Input bar 12
Attack_Group = st.number_input("Enter Attack_Group'")

# Input bar 13
Weapon = st.number_input("Enter Weapon")

# Input bar 14
Number_of_Killed = st.number_input("Enter Number_of_Killed")


# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    clf = joblib.load("classifier1.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[Year, Month, Day, Extended, Country, Region, Suicide,Attack_Type, Target_Type, individual, Nationality_target, Attack_Group, Weapon, Number_of_Killed]], 
                     columns = ['Year', 'Month', 'Day', 'Extended', 'Country', 'Region', 'Suicide',
       'Attack_Type', 'Target_Type', 'individual', 'Nationality_target',
       'Attack_Group', 'Weapon', 'Number_of_Killed'])
   
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    if prediction == 1:
        prediction="Successful Terrorist Attack"
    else:
        prediction="Unsuccessful Terrorist Attack"
   
    
    #Output prediction
    st.text(f"The prediction is a {prediction}")