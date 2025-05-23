import streamlit as st
import pandas as pd
from datetime import datetime
import requests


API_URL = "http://localhost:8000"


def analytics_tab_2():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024,8,1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024,8,5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
        }
        #response = requests.post(url=API_URL, json=payload)
        response = requests.post(f"{API_URL}/analytics/", json=payload)
        response = response.json()

        #st.write(response)

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage":[response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown by Category")
        st.bar_chart(data = df_sorted.set_index("Category")['Percentage'])



        st.table(df_sorted)


