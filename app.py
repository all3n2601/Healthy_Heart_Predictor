import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))



with st.sidebar:
    
    selected = option_menu('Healthy Heart Prediction System',
                          
                          ['Healthy Heart Prediction'],
                          icons=['heart'],
                          default_index=0)
    


# Heart Disease Prediction Page
if (selected == 'Healthy Heart Prediction'):
    
  
    st.title('Healthy Heart Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.selectbox("Sex : 0=female; 1=male",[0,1])
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.selectbox("Resting Electrocardiographic results",[0,1])
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.selectbox("Exercise Induced Angina",[0,1])
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.selectbox("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect",[0,1,2])
    
    
    
    heart_diagnosis = ''
    
    if st.button('Healthy Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                         
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is not Healthy 🫀 and Has a Heart Disease🙁'
        else:
          heart_diagnosis = 'The person is Healthy 🫀 🥳'
        
    st.success(heart_diagnosis)
        
    
