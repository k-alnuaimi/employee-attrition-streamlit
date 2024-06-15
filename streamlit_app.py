import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import pickle as pkl

st.write("Hellow worlds")
with st.sidebar:
    monthlyIncome = st.number_input ("Monthly Income ($)",0,500000,1000,1)
    maritalStatus = st.selectbox("Marital Status",("Single","Married"))
    environmentSatisfaction = st.selectbox("Environment Satisfaction",("Very Satisfied","Satisfied","Disatisfied","Very Disatisfied"))
    yearsWithCurrentManager = st.number_input ("No. Years With Current Manager",0,20,1,1)
    Age = st.number_input ("Age",18,60,20,1)
    jobSatisfaction = st.selectbox("Job Satisfaction",("Very Satisfied","Satisfied","Disatisfied","Very Disatisfied"))