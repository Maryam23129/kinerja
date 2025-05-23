# app.py
import streamlit as st
from modules.financial_metrics import display_financials
from modules.ratios import display_ratios
from modules.forecasting import display_forecast
from modules.debt_profile import display_debt_profile
from modules.strategy import display_strategy

st.set_page_config(page_title="Dashboard Keuangan ASDP", layout="wide")
st.title("Dashboard Kinerja Keuangan - PT ASDP Indonesia Ferry")

menu = st.sidebar.radio("Navigasi", (
    "Kinerja Keuangan",
    "Rasio Keuangan",
    "Forecast Cashflow",
    "Profil Hutang",
    "Strategi Perusahaan"
))

if menu == "Kinerja Keuangan":
    display_financials()
elif menu == "Rasio Keuangan":
    display_ratios()
elif menu == "Forecast Cashflow":
    display_forecast()
elif menu == "Profil Hutang":
    display_debt_profile()
elif menu == "Strategi Perusahaan":
    display_strategy()
