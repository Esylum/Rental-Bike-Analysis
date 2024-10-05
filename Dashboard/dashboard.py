# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='dark')

# Load datasets
hari_df = pd.read_csv("Dashboard/day.csv")
jam_df = pd.read_csv("Dashboard/hour.csv")

# Data cleaning and renaming columns
hari_df.drop(columns=['instant', 'windspeed', 'casual', 'registered', 'hum', 'temp', 'atemp', 'yr'], inplace=True)
jam_df.drop(columns=['instant', 'windspeed', 'casual', 'registered', 'hum', 'temp', 'atemp', 'yr', 'mnth', 'season', 'weathersit'], inplace=True)

hari_df.rename(columns={'dteday': 'tanggal', 'mnth': 'bulan', 'weathersit': 'cuaca', 'season': 'musim', 'cnt': 'jumlah'}, inplace=True)
jam_df.rename(columns={'dteday': 'tanggal', 'hr': 'jam', 'cnt': 'jumlah'}, inplace=True)

# Mapping numbers to categorical values
hari_df['bulan'] = hari_df['bulan'].map({
    1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni', 7: 'Juli',
    8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
})

hari_df['musim'] = hari_df['musim'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
hari_df['cuaca'] = hari_df['cuaca'].map({1: 'Cerah', 2: 'Berawan', 3: 'Hujan', 4: 'Badai'})

# Helper functions for aggregating data
def create_rental_harian_df(df):
    return df.groupby('tanggal').agg({'jumlah': 'sum'}).reset_index()

def create_rental_musiman_df(df):
    return df.groupby('musim')[['jumlah']].sum().reset_index()

def create_rental_cuaca_df(df):
    return df.groupby('cuaca')[['jumlah']].sum().reset_index()

def create_rental_bulanan_df(df):
    rental_bulanan_df = df.groupby('bulan').agg({'jumlah': 'sum'})
    ordered_months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    rental_bulanan_df = rental_bulanan_df.reindex(ordered_months, fill_value=0)
    return rental_bulanan_df

# Sidebar with date range selection
min_date = pd.to_datetime(hari_df['tanggal']).dt.date.min()
max_date = pd.to_datetime(hari_df['tanggal']).dt.date.max()

with st.sidebar:
    st.image('Dashboard/Esylum Rent.png')

start_date, end_date = st.date_input(
    label='Rentang Waktu',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date])

main_df = hari_df[(pd.to_datetime(hari_df['tanggal']).dt.date >= start_date) &
                  (pd.to_datetime(hari_df['tanggal']).dt.date <= end_date)]

# Create dataframes for the filtered period
rental_harian_df = create_rental_harian_df(main_df)
rental_musiman_df = create_rental_musiman_df(main_df)
rental_cuaca_df = create_rental_cuaca_df(main_df)
rental_bulanan_df = create_rental_bulanan_df(main_df)

# Dashboard layout
st.header('Bike Rental Dashboard 🚲')

# Rental Harian section
st.subheader('Rental Harian')
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('Total User', value=rental_harian_df['jumlah'].sum())

# Monthly Rentals
st.subheader('Rental Bulanan')

# Check if 'jumlah' column exists in rental_bulanan_df
if 'jumlah' in rental_bulanan_df.columns:
    fig, ax = plt.subplots(figsize=(24, 8))
    
    # Bar plot for monthly rentals
    sns.barplot(x=rental_bulanan_df.index, y='jumlah', data=rental_bulanan_df)
    
    # Add text labels on bars
    for index, row in rental_bulanan_df.iterrows():
        ax.text(index, row['jumlah'] + 1, str(row['jumlah']), ha='center', va='bottom', fontsize=12)
    
    ax.tick_params(axis='x', labelsize=25, rotation=45)
    ax.tick_params(axis='y', labelsize=20)
    st.pyplot(fig)

# Seasonal Rentals
st.subheader('Rental Musiman')
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x='musim', y='jumlah', data=rental_musiman_df)

for index, row in rental_musiman_df.iterrows():
    ax.text(index, row['jumlah'] + 1, str(row['jumlah']), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

# Weather-based Rentals
st.subheader('Rental Cuaca')
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x='cuaca', y='jumlah', data=rental_cuaca_df)

for index, row in rental_cuaca_df.iterrows():
    ax.text(index, row['jumlah'] + 1, str(row['jumlah']), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

st.caption('Copyright (c) Brigade Mahendra 2024')
