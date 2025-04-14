import streamlit as st
import pandas as pd
from datetime import datetime
import requests


API_URL = "http://localhost:8000"


def analytics_tab_3():
    response = requests.get(f"{API_URL}/monthly_summary/")

    if response.status_code != 200:
        st.error("Failed to fetch monthly summary")
        return

    monthly_summary = response.json()

    # This assumes monthly_summary is a list of dicts like:
    # [{"expense_month": 8, "month_name": "August", "total": 5145.0}, {...}]
    df = pd.DataFrame(monthly_summary)

    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)

    df_sorted = df.sort_values(by="Month Number", ascending=True)

    st.title("Expense Breakdown By Months")

    # Bar chart: x = Month Name, y = Total
    st.bar_chart(data=df_sorted.set_index("Month Name")["Total"])

    # Format totals to 2 decimal places (just for display in the table)
    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    st.table(df_sorted)