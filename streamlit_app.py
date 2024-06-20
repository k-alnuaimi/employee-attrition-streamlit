import pandas as pd
import streamlit as st

@st.cache_resource
def init_model():
    return pd.read_pickle("random-forest-attrition.pkl")
model_rf = init_model()

st.set_page_config(initial_sidebar_state='collapsed')

def show_turnover_rate():
    data = {'Age' : Age,
            'BusinessTravel_Travel_Frequently' : businessTravel == "Travel Frequently", 
            'BusinessTravel_Travel_Rarely':  businessTravel == "Travel Rarely",
       'Department_Research & Development': department == "R&D",
         'Department_Sales': department == "Sales",
               'DistanceFromHome' : round(distanceFromeHome * 0.6),
                         'Education' : education,
                                     'EnvironmentSatisfaction' : satisfactionOptions.index(environmentSatisfaction)+1,
           'Gender_Male' : gender == "Male",
                  'JobInvolvement' : jobInvolvement,
                           'JobLevel' : jobLevel,
       'JobRole_Human Resources' : jobRole == "HR",
         'JobRole_Laboratory Technician' : jobRole == "LAB TECHNICIAN",
       'JobRole_Manager' : jobRole == "MANAGER",
         'JobRole_Manufacturing Director' : jobRole == "MANAGING DIRECTOR",
       'JobRole_Research Director' : jobRole == "REASEARCH DIRECTOR",
         'JobRole_Research Scientist' : jobRole == "RESEARCH SCIENTIST",
       'JobRole_Sales Executive' : jobRole == "SALES EXECUTIEVE",
         'JobRole_Sales Representative' : jobRole == "SALES REPRESENTATIVE",
                    'JobSatisfaction': satisfactionOptions.index(jobSatisfaction)+1 ,
       'MaritalStatus_Married' : maritalStatus == "Married",
         'MaritalStatus_Single': maritalStatus == "Single",
                      'MonthlyIncome' : monthlyIncome,
                             'NumCompaniesWorked' : numCompaniesWorked,
           'OverTime_Yes': overTime=="Yes", 
         'PercentSalaryHike' : percentSalaryHike,
           'PerformanceRating' : performanceRating,
       'RelationshipSatisfaction' : relationShipSatisfaction,
         'TotalWorkingYears' : totalWorkingYears,
       'TrainingTimesLastYear' : trainingTimesLastYear,
         'WorkLifeBalance' : workLifeBalance,
           'YearsAtCompany' : yearsAtCompnay,
       'YearsInCurrentRole' : yearsInCurrentRole,
         'YearsSinceLastPromotion' : yearsSinceLastPromotion,
       'YearsWithCurrManager' : yearsWithCurrentManager}
    df = pd.DataFrame(data,index=[0])
    df.replace({False: 0, True: 1}, inplace=True)
    turnover_prediction = model_rf.predict_proba(df)
    st.write('There is a', turnover_prediction[0][1] * 100 ,'% chance of the employee leaving')
showrate = False
    

col1, col2, col3 = st.columns(3)
with st.form(key='my_form'):
    with col1:
        monthlyIncome = st.slider("Monthly Income ($)",0,100000,6500,500)
        maritalStatus = st.selectbox("Marital Status",("Single","Married","Divorced"))
        satisfactionOptions = ["Very Disatisfied","Disatisfied","Satisfied","Very Satisfied"]
    with col2:
        environmentSatisfaction = st.selectbox("Environment Satisfaction",satisfactionOptions,2)
        yearsAtCompnay = st.number_input ("No. Years At Company",0,50,5,1)
        yearsWithCurrentManager = st.number_input ("No. Years With Current Manager",0,50,3,1)
    with col3:
        Age = st.number_input ("Age",18,60,35,1)
        jobSatisfaction = st.selectbox("Job Satisfaction",satisfactionOptions,1)
        distanceFromeHome = st.slider("Distance From Home (KM)",1,200,4,1)
    submit_button = st.form_submit_button("Submit")
    with st.sidebar:
        
        #don't forget to convert to miles ( multiply by 0.6 )
        totalWorkingYears = st.slider("Total Working Years",0,60,6,1)
        yearsInCurrentRole = st.slider("Years In Current Role",0,60,3,1)
        workLifeBalance = st.slider("Work Life Balance",1,4,1,1)
        jobInvolvement = st.slider("Job Involvement",1,4,2,1)
        relationShipSatisfaction = st.slider("Relationship Satisfaction",1,4,2,1)
        department =st.selectbox("Department",("Sales","HR","R&D"))
        jobLevel = st.slider("Job Level",1,5,2,1)
        trainingTimesLastYear = st.slider("Training Times Last year",1,10,2,1)
        percentSalaryHike = st.slider("Percentage Increase In Salary ",1,30,5,1)
        numCompaniesWorked = st.slider("Number of Compnaies Worked",1,10,2,1)
        education = st.slider("Education",1,5,3,1)
        yearsSinceLastPromotion = st.slider("Years Since Last Promotion",1,30,2,1)
        businessTravel = st.selectbox("Business Travel",("No Travel","Travel Frequently","Travel Rarely"))
        jobRole = st.selectbox("Job Role",("HC REP","HR","LAB TECHNICIAN","MANAGER","MANAGING DIRECTOR","REASEARCH DIRECTOR","RESEARCH SCIENTIST","SALES EXECUTIEVE","SALES REPRESENTATIVE"))
        gender = st.selectbox("Gender",("Male","Female"))
        overTime =st.selectbox("OverTime",("Yes","No"))
        performanceRating = st.slider("Performance Rating",1,5,2,1)

    if submit_button:
      showrate = True
    else:
      showrate = False
if showrate:
  show_turnover_rate()
  

