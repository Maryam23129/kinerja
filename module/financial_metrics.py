import streamlit as st
import pandas as pd

def display_financials():
    st.header("Kinerja Keuangan")
    data = {
        "Item": ["Pendapatan", "EBITDA", "Fixed Cost", "Laba Bersih", "Debt"],
        "Nilai (Miliar IDR)": [1500, 450, 300, 200, 1000]
    }
    df = pd.DataFrame(data)
    st.table(df)