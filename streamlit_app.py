import pandas as pd
import streamlit as st

st.set_page_config(initial_sidebar_state='collapsed')
@st.cache_resource
def init_model():
    return pd.read_pickle("random-forest-attrition.pkl")
model_rf = init_model()

satisfactionOptions = ["Very Disatisfied","Disatisfied","Satisfied","Very Satisfied"]


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
    probability = round(turnover_prediction[0][1] * 100)
    text = ''
    img = ''
    if probability < 33:
        img = 'Happy Employee 1.jpeg'
        text = 'Happy Employee'
    elif probability < 66:
        img = 'Normal Employee.jpeg'
        text = 'Normal Employee'
    else:
        text = 'Employee likely to leave'
        img = 'Sad Employee 1.jpeg'
    col1, col2 = st.columns([0.35,0.65])
    with col1:
        st.subheader(text)
    with col2:
        st.image(img)
    
    

col1, col2, col3 = st.columns(3)
#with st.form(key='my_form'):
with col1:
    monthlyIncome = st.slider("Monthly Income ($)",0,50000,3000,500)
    maritalStatus = st.selectbox("Marital Status",("Single","Married","Divorced"))
    #totalWorkingYears = st.slider("Total Working Years",0,30,6,1)
with col2:
    environmentSatisfaction = st.selectbox("Environment Satisfaction",satisfactionOptions,2)
    #yearsAtCompnay = st.number_input ("No. Years At Company",0,30,3,1)
    #yearsWithCurrentManager = st.number_input ("No. Years With Current Manager",0,30,1,1)
    workLifeBalance = st.slider("Work Life Balance",1,4,1,1)
    performanceRating = st.slider("Performance Rating",1,5,2,1)
    submit_button = st.button("Submit",type="primary")
with col3:
    Age = st.number_input ("Age",18,60,25,1)
    jobSatisfaction = st.selectbox("Job Satisfaction",satisfactionOptions,1)
    distanceFromeHome = st.slider("Distance From Home (KM)",1,200,4,1)
with st.sidebar:
    gender = st.selectbox("Gender",("Male","Female"))
    overTime =st.selectbox("OverTime",("Yes","No"))
    businessTravel = st.selectbox("Business Travel",("No Travel","Travel Frequently","Travel Rarely"))
    
    #yearsInCurrentRole = st.slider("Years In Current Role",0,60,1,1)
    yearsInCurrentRole = 0
    
    
    jobInvolvement = st.slider("Job Involvement",1,4,2,1)
    relationShipSatisfaction = st.slider("Relationship Satisfaction",1,4,2,1)
    #department =st.selectbox("Department",("Sales","HR","R&D"))
    department = "HR"
    #jobLevel = st.slider("Job Level",1,5,2,1)
    jobLevel = 1
    trainingTimesLastYear = st.slider("Training Times Last year",1,10,2,1)
    percentSalaryHike = st.slider("Percentage Increase In Salary ",1,30,5,1)
    numCompaniesWorked = st.slider("Number of Compnaies Worked",1,10,2,1)
    #education = st.slider("Education",1,5,3,1)
    education = 1
    #yearsSinceLastPromotion = st.slider("Years Since Last Promotion",1,30,2,1)
    yearsSinceLastPromotion = 1
    #jobRole = st.selectbox("Job Role",("HC REP","HR","LAB TECHNICIAN","MANAGER","MANAGING DIRECTOR","REASEARCH DIRECTOR","RESEARCH SCIENTIST","SALES EXECUTIEVE","SALES REPRESENTATIVE"))
    jobRole = "HR"
    yearsWithCurrentManager = 0
    yearsAtCompnay = 0
    totalWorkingYears  = 2
   # if submit_button:
  #    showrate = True
  #  else:
  #    showrate = False

if submit_button:
  show_turnover_rate()
  

