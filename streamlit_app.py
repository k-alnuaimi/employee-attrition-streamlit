import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.write("Hellow worlds")
monthlyIncome = st.number_input ("Monthly Income ($)",0,500000,1000,1)
maritalStatus = st.selectbox("Marital Status",("Single","Married"))
environmentSatisfaction = st.selectbox("Environment Satisfaction",("Very Satisfied","Satisfied","Disatisfied","Very Disatisfied"))
yearsWithCurrentManager = st.number_input ("No. Years With Current Manager",0,20,1,1)
st.write('test')