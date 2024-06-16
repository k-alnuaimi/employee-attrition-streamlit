import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pickle as pkl


with st.form(key='my_form'):
    with st.sidebar:
        monthlyIncome = st.number_input ("Monthly Income ($)",0,500000,1000,1)
        maritalStatus = st.selectbox("Marital Status",("Single","Married","Divorced"))
        environmentSatisfaction = st.selectbox("Environment Satisfaction",("Very Satisfied","Satisfied","Disatisfied","Very Disatisfied"))
        yearsAtCompnay = st.number_input ("No. Years At Company",0,50,5,1)
        yearsWithCurrentManager = st.number_input ("No. Years With Current Manager",0,yearsAtCompnay,2,1)
        Age = st.number_input ("Age",18,60,20,1)
        jobSatisfaction = st.selectbox("Job Satisfaction",("Very Satisfied","Satisfied","Disatisfied","Very Disatisfied"))
        submit_button = st.form_submit_button("Submit")
        with st.expander("Additional Fields"):
            #don't forget to convert to miles ( multiply by 0.6 )
            distanceFromeHome = st.slider("Distance From Home (KM)",1,200,2,1)
            totalWorkingYears = st.slider("Total Working Years",yearsAtCompnay,60,1,yearsAtCompnay)
            yearsInCurrentRole = st.slider("Years In Current Role",0,60,1,1)
            workLifeBalance = st.slider("Work Life Balance",1,4,1,2)
            jobInvolvement = st.slider("Job Involvement",1,4,1,2)
            relationShipSatisfaction = st.slider("Relationship Satisfaction",1,4,1,2)
            department =st.selectbox("Department",("Sales","HR","R&D"))
            jobLevel = st.slider("Job Level",1,5,1,2)
            trainingTimesLastYear = st.slider("Training Times Last year",1,10,1,2)
            percentSalaryHike = st.slider("Percentage Increase In Salary ",1,30,1,5)
            numCompaniesWorked = st.slider("Number of Compnaies Worked",1,10,1,1)
            education = st.slider("Education",1,5,1,3)
            yearsSinceLastPromotion = st.slider("Years Since Last Promotion",1,yearsAtCompnay,1,1)
            businessTravel = st.selectbox("Business Travel",("No Travel","Travel Frequently","Travel Rarely"))
            jobRole = st.selectbox("Job Role",("HC REP","HR","LAB TECHNICIAN","MANAGER","MANAGING DIRECTOR","REASEARCH DIRECTOR","RESEARCH SCIENTIST","SALES EXECUTIEVE","SALES REPRESENTATIVE"))
            gender = st.selectbox("Gender",("Male","Female"))
            overTime =st.selectbox("OverTime",("Yes","No"))
            performanceRating = st.slider("Performance Rating",1,5,1,3)
if submit_button:
    st.write("Hellow worlds")