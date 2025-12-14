import streamlit as st
import pandas as pd
from weather import get_weather_data

st.set_page_config(page_title="Weather vs Food Orders", layout="centered")

st.title("🍔 Weather vs Food Orders Dashboard")

# Load food order data
orders_df = pd.read_csv("orders.csv")

# Fetch live weather data
weather = get_weather_data()

# Display weather info
st.subheader("🌦️ Today's Weather")
st.write(f"**Date:** {weather['date']}")
st.write(f"**Temperature:** {weather['temperature']} °C")
st.write(f"**Condition:** {weather['condition']}")

# Display food orders chart
st.subheader("📊 Food Orders Trend")
st.line_chart(orders_df.set_index("date"))

# Simple insight
st.subheader("🔍 Insight")
if weather["is_rainy"] == 1:
    st.success("Orders tend to increase on rainy days 🌧️")
else:
    st.info("Orders are moderate on clear days ☀️")

