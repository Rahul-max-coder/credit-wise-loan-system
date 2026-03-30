import streamlit as st
import pandas as pd

st.title("Credit Wise Loan System")

st.write("Loan Data Preview")

df = pd.read_csv("loan_approvel_data.csv")

st.write(df.head())
