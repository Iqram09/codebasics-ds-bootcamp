import streamlit as st
from analytics_tab import analytics_tab
from analytics_tab_2 import analytics_tab_2
from analytics_tab_3 import analytics_tab_3

st.title("Expense Management System")

tab1, tab2 ,tab3 = st.tabs(["Add/Update","Analytics","Analytics by month"])

with tab1:
    analytics_tab()

with tab2:
    analytics_tab_2()

with tab3:
    analytics_tab_3()
