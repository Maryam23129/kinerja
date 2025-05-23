import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def display_forecast():
    st.header("Forecast Cashflow 2 Minggu")
    today = datetime.today()
    dates = [today + timedelta(days=i) for i in range(14)]
    cashflow = np.random.randint(100, 500, size=14)
    df = pd.DataFrame({ "Tanggal": dates, "Cashflow (Juta IDR)": cashflow })
    st.line_chart(df.set_index("Tanggal"))