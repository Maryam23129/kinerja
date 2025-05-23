import streamlit as st
import pandas as pd

def display_debt_profile():
    st.header("Profil Hutang")
    data = {
        "Jenis Hutang": ["Bank A", "Bank B", "Obligasi"],
        "Jumlah (Miliar IDR)": [400, 300, 300],
        "Jatuh Tempo": ["2027", "2025", "2028"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)