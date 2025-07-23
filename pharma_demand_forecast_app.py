# app.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from prophet import Prophet
import streamlit as st

st.set_page_config(page_title="Pharma Demand Forecasting", layout="wide")

st.title("📈 Pharmaceutical Demand Forecasting")

# Upload or auto-load
uploaded_file = st.file_uploader("Upload sales CSV", type=['csv'])

if uploaded_file or os.path.exists("data/sample_demand_data.csv"):
    # Load data
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("data/sample_demand_data.csv")

    # Preprocessing
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna(subset=['sales'])
    df = df[df['sales'] >= 0]
    df = df.groupby('date').agg({'sales': 'sum'}).reset_index()
    df = df.rename(columns={'date': 'ds', 'sales': 'y'})

    st.subheader("📊 Cleaned Time Series Data")
    st.dataframe(df.tail())

    # Forecasting
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    st.subheader("📉 Forecast Plot")
    fig = model.plot(forecast)
    st.pyplot(fig)

    # Download forecast
    forecast_out = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    csv = forecast_out.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Forecast CSV", csv, "forecast_output.csv", "text/csv")

else:
    st.warning("Please upload a valid CSV or place `sample_demand_data.csv` in the `data/` folder.")
