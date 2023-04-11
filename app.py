import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))



with st.sidebar:
    
    selected = option_menu('Healthy Heart Prediction System',
                          
                          ['Healthy Heart Prediction'],
                          icons=['heart'],
                          default_index=0)
    
    st.subheader("Note :")
    st.caption("0 = FALSE")
    st.caption("1 = TRUE")
    st.caption("Name : M A ALLEN FEBI")
    st.caption("Reg No : 21BCE7470")
    


# Heart Disease Prediction Page
if (selected == 'Healthy Heart Prediction'):
    
  
    st.title('Healthy Heart Prediction using ML')
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age",10,100)
        
    with col2:
        trestbps = st.slider('Resting Blood Pressure',94,200)    
        
    with col2:
        sex = st.selectbox("Sex : 0=female; 1=male                                                                  .",[0,1])
        
    with col1:
        cp = st.selectbox('Chest Pain types 1=typical angina, 2=atypical angina, 3=non-angina, 4=asymptomatic angina',[0,1,2,3,4])
        
        
    with col1:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",[0,1])
        
    with col1:
        restecg = st.selectbox("Resting Electrocardiographic results",[0,1])
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col1:
        exang = st.selectbox("Exercise Induced Angina",[0,1])
        
    with col2:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col1:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col2:
        ca = st.number_input('Major vessels colored by flouroscopy')
        
    with col1:
        thal = st.selectbox("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect",[0,1,2])
    
    
    
    heart_diagnosis = ''
    
    if st.button('Healthy Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                         
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = "The person is not Healthy 🫀 and Has a Heart Disease Try Following The Diet \n"
          st.write(
                              '''-----------------------------------------------------------------------------------------------------
                        \t\t Sunday    | Monday  |  Tuesday  |  Wednesday  |  Thursday  |  Friday  |  Saturday  |
        
        ------------------------------------------------------------------------------------------------------
        
        BreakFast |
        
        ------------------------------------------------------------------------------------------------------
        
        Lunch     |
        
        ------------------------------------------------------------------------------------------------------
        
        Dinner    |
        
        ------------------------------------------------------------------------------------------------------'''
              
          )
        else:
          heart_diagnosis = 'The person is Healthy 🫀 🥳'
        
    st.success(heart_diagnosis)
        
    
