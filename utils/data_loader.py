import streamlit as st
import pandas as pd
import json
import os

@st.cache_data
def load_raw_data():
    if os.path.exists('train.csv'):
        df = pd.read_csv('train.csv')
        df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
        df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')
        df['Year'] = df['Order Date'].dt.year
        df['Month'] = df['Order Date'].dt.month
        df['ShipDelay'] = (df['Ship Date'] - df['Order Date']).dt.days
        return df.dropna(subset=['Order Date', 'Ship Date'])
    return None

@st.cache_data
def load_cache_data():
    if os.path.exists('streamlit_cache.json'):
        with open('streamlit_cache.json', 'r') as f:
            return json.load(f)
    return None
