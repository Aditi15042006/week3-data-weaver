# Week 3 – The Data Weaver 📊

## Project Title
Weather vs Food Orders Dashboard

---

## Problem Statement
Food delivery demand is influenced by many external factors.  
This project explores whether **weather conditions**, especially rain, have any effect on **food ordering behavior**.

---

## Solution
A simple dashboard that mashes up:
- 🌦️ **Live weather data** (OpenWeatherMap API)
- 🍔 **Food order data** (mock CSV dataset)

The dashboard visually compares food order trends and provides insights based on current weather conditions.

---

## Tech Stack
- Python
- Streamlit
- Pandas
- OpenWeatherMap API

---

## Data Sources
1. **Weather Data**
   - Source: OpenWeatherMap API
   - Data: Temperature, weather condition, rain detection

2. **Food Orders Data**
   - Source: Mock dataset (`orders.csv`)
   - Data: Date-wise number of orders

---

## Dashboard Features
- Displays today’s live weather
- Line chart of food orders
- Insight indicating impact of rainy vs clear days

---

## How Kiro Helped
Kiro assisted throughout the development by:
- Suggesting the idea of combining unrelated datasets
- Helping structure the dashboard logic
- Refining insights and presentation approach

All prompts, decisions, and iterations are documented in the `.kiro` directory.

---

## How to Run (Optional)
```bash
pip install -r requirements.txt
streamlit run app.py

