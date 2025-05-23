import streamlit as st
import pandas as pd

def display_ratios():
    st.header("Rasio Keuangan")
    data = {
        "Rasio": ["DSCR", "Current Ratio", "DER", "ROE", "ROA"],
        "Nilai": [1.5, 2.0, 1.2, 15, 8]
    }
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Rasio"))