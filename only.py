import streamlit as st
import pandas as pd


st.title("Expense Management System")

expense_dt = st.date_input("Enter expense date")
if expense_dt:
    st.write(f"Fetching expenses: {expense_dt}")

#data display test
st.subheader("Expense Details")
st.write("Here is a table of expenses:")
df = pd.DataFrame({
    "Date": ["2024-08-01", "2024-08-02", "2024-08-03"],
    "Amount": [160, 278, 390],
})
st.table(df)

#charts test
st.subheader("Charts")
st.line_chart([1,2,3,4,5])

#input test
st.subheader("User Input")
value = st.slider("Select a Value", min_value=100, max_value=1000, step=10)
st.write(f"Select Value: {value}")

#check box
if st.checkbox("Show/Hide"):
    st.write("Checkbox is Selected :)")

#select box test
option = st.selectbox("Select Option", options=[1, 2, 3, 4, 5])
st.write(f"Select Option: {option}")

#multiselect box
option = st.multiselect("Select Option", options=[1, 2, 3, 4, 5])
st.write(f"Select Option: {option}")