import streamlit as st
import pandas as pd

def display_financials():
    st.header("Kinerja Keuangan")
    df = pd.DataFrame({
        "Item": ["Pendapatan", "EBITDA", "Fixed Cost", "Laba Bersih", "Debt"],
        "Nilai (Miliar IDR)": [1500, 450, 300, 200, 1000]
    })
    st.table(df)
