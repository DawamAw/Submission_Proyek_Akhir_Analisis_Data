import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(st.__version__)

# Mengatur tampilan halaman
st.set_page_config(page_title="Bike Rental Dashboard", layout="wide")

# Sidebar untuk filter interaktif
st.sidebar.title("Pengaturan Dashboard")
day_filter = st.sidebar.selectbox("Pilih Hari", ["Semua Hari", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
weather_filter = st.sidebar.selectbox("Pilih Cuaca", ["Semua Cuaca", "Cerah", "Berawan", "Hujan", "Berkabut"])
season_filter = st.sidebar.selectbox("Pilih Musim", ["Semua Musim", "Musim Dingin", "Musim Semi", "Musim Panas", "Musim Gugur"])

# Judul Utama Dashboard
st.title("📊 Bike Rental Analysis Dashboard")
st.markdown("Dashboard ini menampilkan berbagai visualisasi data terkait penyewaan sepeda berdasarkan data historis. Kamu bisa menggunakan sidebar untuk menyesuaikan filter sesuai preferensi.")

# Contoh data untuk digunakan
# Data Dummy sesuai dengan pertanyaan, ganti dengan data asli sesuai penggunaan
data_rentals = {
    'Day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    'Weather': ['Clear', 'Partly Cloudy', 'Rain', 'Clear', 'Partly Cloudy', 'Rain', 'Clear'],
    'Season': ['Winter', 'Spring', 'Summer', 'Fall', 'Winter', 'Spring', 'Summer'],
    'Registered': [3912, 3500, 4200, 3800, 4600, 3000, 4500],
    'Casual': [800, 500, 300, 400, 550, 200, 750],
    'Count': [4712, 4000, 4500, 4200, 5150, 3200, 5250]
}

df = pd.DataFrame(data_rentals)

# Filter data berdasarkan pilihan pengguna
if day_filter != "Semua Hari":
    df = df[df['Day'] == day_filter]

if weather_filter != "Semua Cuaca":
    df = df[df['Weather'] == weather_filter]

if season_filter != "Semua Musim":
    df = df[df['Season'] == season_filter]

# Membagi layar menjadi dua kolom
col1, col2 = st.columns(2)

# Grafik 1: Bar plot penyewaan terdaftar dan kasual
with col1:
    st.markdown("### 📊 Penyewaan Sepeda Berdasarkan Pengguna Terdaftar dan Kasual")
    fig1, ax1 = plt.subplots()
    df[['Registered', 'Casual']].plot(kind='bar', ax=ax1)
    plt.title("Penyewaan Terdaftar vs Kasual")
    plt.ylabel("Jumlah Penyewaan")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

# Grafik 2: Penyewaan berdasarkan cuaca
with col2:
    st.markdown("### 🌦️ Penyewaan Berdasarkan Cuaca")
    fig2, ax2 = plt.subplots()
    sns.barplot(data=df, x='Weather', y='Count', ax=ax2, palette='coolwarm')
    plt.title("Penyewaan Berdasarkan Cuaca")
    st.pyplot(fig2)

# Row 2: Scatter Plot & Line Plot
col3, col4 = st.columns(2)

# Grafik 3: Scatter plot suhu vs jumlah penyewaan
with col3:
    st.markdown("### 🌡️ Hubungan Suhu, Kelembapan, dan Penyewaan")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x='Registered', y='Count', size='Casual', hue='Weather', palette='coolwarm', ax=ax3)
    plt.title("Hubungan Antara Jumlah Penyewaan Terdaftar dan Kasual")
    st.pyplot(fig3)

# Grafik 4: Line plot berdasarkan musim
with col4:
    st.markdown("### 🍂 Pola Penyewaan Berdasarkan Musim")
    fig4, ax4 = plt.subplots()
    sns.lineplot(data=df, x='Season', y='Count', marker='o', ax=ax4)
    plt.title("Pola Penyewaan Berdasarkan Musim")
    plt.ylabel("Total Penyewaan")
    st.pyplot(fig4)

# Kesimpulan akhir di bagian bawah
st.markdown("## Kesimpulan Utama")
st.markdown("""
1. Penyewaan sepeda paling tinggi terjadi pada musim panas, sementara penyewaan terendah terjadi di musim dingin.
2. Cuaca cerah dan sedikit mendung cenderung meningkatkan jumlah penyewaan sepeda, sementara hujan menurunkan penyewaan, terutama pada pengguna kasual.
3. Pengguna terdaftar cenderung lebih konsisten dalam melakukan penyewaan sepeda, sedangkan pengguna kasual sangat dipengaruhi oleh kondisi cuaca.
4. Pada hari libur, jumlah penyewaan dari pengguna kasual meningkat signifikan dibandingkan hari kerja, sementara pengguna terdaftar mendominasi pada hari kerja.
""")
