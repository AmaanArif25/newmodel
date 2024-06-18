# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: amaan arif
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

dementia = pickle.load(open('dementia_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('SMIRTI-D',
                          
                          ['Dementia Disease Prediction',
                          icons=['brain'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Dementia Disease Prediction'):
    
    # page title
    st.title('Dementia Disease using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        EDU = st.text_input('Education level (usually measured in years of formal education) ')
    
    with col3:
        SES = st.text_input('Socioeconomic Status')
    
    with col1:
       MMSE  = st.text_input('Mini-Mental State Examination (a measure of cognitive function)')
    
    with col2:
        CDR = st.text_input('Clinical Dementia Rating')
    
    with col3:
        eTIV = st.text_input('Estimated Total Intracranial Volume ')
    
    with col1:
        nWBV = st.text_input('Normalized Whole Brain Volume')
    
    with col2:
        ASF = st.text_input('Atlas Scaling Factor')
    
    
    # code for Prediction
    demen_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Dementia Test Result'):
        demen_prediction = dementia_model.predict([[Age, EDUC, SES, MMSE, CDR, eTIV, nWBV, ASF]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is having Dementia'
        else:
          diab_diagnosis = 'The person is not having dementia'
        
    st.success(demen_diagnosis)

















