import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    hari_df = pd.read_csv("Dashboard/day.csv")
    jam_df = pd.read_csv("Dashboard/hour.csv")
    
    # Preprocess the data as you did in the script
    hari_df.drop(columns=['instant', 'windspeed', 'casual', 'registered', 'hum', 'temp', 'atemp', 'yr'], inplace=True)
    hari_df.rename(columns = {
        'dteday':'tanggal',
        'mnth':'bulan',
        'weathersit':'cuaca',
        'season':'musim',
        'cnt':'jumlah'
    }, inplace=True)
    
    hari_df['bulan'] = hari_df['bulan'].map({
        1: 'Januari', 2:'Februari', 3:'Maret',
        4:'April', 5:'Mei', 6:'Juni', 7:'Juli',
        8:'Agustus', 9:'September', 10:'Oktober',
        11:'November', 12:'Desember'
    })

    hari_df['musim'] = hari_df['musim'].map({
        1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'
    })

    hari_df['cuaca'] = hari_df['cuaca'].map({
        1:'Cerah', 2:'Berawan', 3:'Hujan', 4:'Badai'
    })
    
    hari_df['tanggal'] = pd.to_datetime(hari_df['tanggal'])
    hari_df['bulan'] = hari_df.bulan.astype('category')
    hari_df['musim'] = hari_df.musim.astype('category')
    hari_df['cuaca'] = hari_df.cuaca.astype('category')
    
    return hari_df, jam_df

# Visualizations
def correlation_heatmap(df):
    st.subheader("Heatmap Korelasi")
    correlation_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    st.pyplot(plt.gcf())

def barplot_rentals(df, x, hue, title, xlabel):
    plt.figure(figsize=(11, 6))
    sns.barplot(x=x, y='Value', hue=hue, data=df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Value')
    st.pyplot(plt.gcf())

# Main Streamlit app
def main():
    # Sidebar content
    with st.sidebar:
        st.image('Dashboard/Esylum Rent.png')  # Cover image in the sidebar

    # Dashboard layout
    st.header('Bike Rental Dashboard 🚲')  # Dashboard header

    # Load data
    hari_df, jam_df = load_data()
    
    st.write("### Data Overview")
    st.write(hari_df.head())

    st.write("### Data Information")
    st.write(hari_df.info())

    st.write("### Jumlah data duplikat: ", hari_df.duplicated().sum())
    st.write("### Descriptive Statistics")
    st.write(hari_df.describe())

    # Heatmap correlation
    correlation_heatmap(hari_df)

    # Data transformation for visualizations
    st.write("### Perbandingan Bulanan (Weekday, Workingday, Holiday)")
    melted_bulan = pd.melt(hari_df, id_vars=['bulan'], value_vars=['weekday', 'workingday', 'holiday'],
                           var_name='Type', value_name='Value')
    barplot_rentals(melted_bulan, 'bulan', 'Type', 'Perbandingan rental bulanan weekday, workingday, dan holiday', 'Bulan')

    st.write("### Pengaruh Cuaca terhadap Rental")
    melted_cuaca = pd.melt(hari_df, id_vars=['cuaca'], value_vars=['weekday', 'workingday', 'holiday'],
                           var_name='Type', value_name='Value')
    barplot_rentals(melted_cuaca, 'cuaca', 'Type', 'Pengaruh cuaca terhadap rental pada weekday, workingday, dan holiday', 'Cuaca')

    st.write("### Pengaruh Musim terhadap Rental")
    melted_musim = pd.melt(hari_df, id_vars=['musim'], value_vars=['weekday', 'workingday', 'holiday'],
                           var_name='Type', value_name='Value')
    barplot_rentals(melted_musim, 'musim', 'Type', 'Pengaruh musim terhadap rental pada weekday, workingday, dan holiday', 'Musim')

    # Add copyright info
    st.write("\n\n© Brigade Mahendra")

if __name__ == "__main__":
    main()
