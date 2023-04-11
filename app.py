import pickle
import streamlit as st
import pandas as pd
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
          heart_diet = pd.DataFrame({
                      'Meal': ['Breakfast', 'Mid-morning snack', 'Lunch', 'Afternoon snack', 'Dinner'],
                      'Monday': ['1 cup oatmeal with fruit and nuts, 1 cup green tea', '1 apple, 10 almonds', 'Grilled chicken breast, steamed veggies, 1 whole grain roll', '1 orange, 1 protein shake', 'Grilled fish, mixed veggies, quinoa'],
                      'Tuesday': ['Greek yogurt with granola and berries, 1 cup of tea', '1 pear, 1 hard-boiled egg', 'Grilled salmon, mixed greens salad, balsamic vinaigrette', '1 cup of green tea, 1 string cheese', 'Grilled chicken, roasted potatoes, mixed veggies'],
                      'Wednesday': ['Egg white omelette with veggies, 1 cup of coffee', '1 banana, 1 hard-boiled egg', 'Grilled shrimp, brown rice, steamed veggies', '1 protein bar, 1 apple', 'Grilled sirloin steak, sweet potato, mixed veggies'],
                      'Thursday': ['Whole grain toast with avocado and smoked salmon, 1 cup of tea', '1 orange, 10 almonds', 'Grilled chicken breast sandwich on whole grain bread, baby carrots', '1 cup of green tea, 1 string cheese', 'Grilled pork tenderloin, roasted potatoes, mixed veggies'],
                      'Friday': ['Egg white scramble with veggies and whole grain toast, 1 cup of coffee', '1 apple, 1 hard-boiled egg', 'Grilled chicken kebab, tabbouleh salad', '1 cup of green tea, 1 protein bar', 'Grilled fish tacos with salsa and avocado, mixed veggies'],
                      })
          st.table(heart_diet)
        else:
          heart_diagnosis = 'The person is Healthy 🫀 🥳'
          healthy_diet = pd.DataFrame({
                        'Meal': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                        'Breakfast': ['2 eggs, whole wheat toast, avocado, and a cup of coffee', 'Greek yogurt with berries and granola', 'Oatmeal with fruit and nuts', 'Whole grain toast with avocado and tomato', 'Scrambled tofu with veggies and whole grain toast', 'Vegetable omelette with whole grain toast', 'Green smoothie with spinach, banana, and almond milk'],
                        'Lunch': ['Mixed greens salad with grilled chicken or tofu, vinaigrette dressing', 'Brown rice and mixed veggies stir-fry with tofu or shrimp', 'Quinoa salad with mixed veggies and chickpeas', 'Lentil soup with whole grain roll', 'Grilled veggie burger with baby carrots', 'Grilled portobello mushroom with mixed veggies and sweet potato', 'Chickpea wrap with hummus and veggies'],
                        'Dinner': ['Grilled salmon or tofu with mixed veggies and quinoa', 'Baked chicken or tofu with sweet potato and mixed greens', 'Vegetable curry with brown rice', 'Turkey chili with mixed greens salad', 'Grilled shrimp skewers with mixed veggies and quinoa', 'Grilled eggplant parmesan with mixed greens salad', 'Black bean burger with mixed greens salad'],
                        })
          st.table(healthy_diet)
    st.success(heart_diagnosis)
        
    
