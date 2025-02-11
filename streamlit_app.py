import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import altair as alt

# --- Sidebar ---
st.sidebar.markdown(
    """
    <div style="display: flex; align-items: center;">
        <img src="https://bit.ly/4hZMzM7" width="50" style="margin-right: 10px;">
        <h1 style="margin: 0;">KELOMPOK 6</h1>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)
# Menu Navigasi
with st.sidebar:
    selected = option_menu(
        menu_title="Dashboard",
        options=["Home", "Menu 1", "Menu 2", "Menu 3", "Menu 4", "Menu 5", "Menu 6", "Menu 7"],
        icons=["house", "eye", "eye", "eye", "eye", "eye", "eye", "eye"],
        menu_icon="cast",
        default_index=0
    )

#Data
data_day = pd.read_csv('day.csv')
data_hour = pd.read_csv('hour.csv')

# Mengubah 'dteday' ke datetime (Konversi Tanggal)
data_day['dteday'] = pd.to_datetime(data_day['dteday'])

# Membuat kolom baru yang menggabungkan bulan dan tahun
data_day['yr_month'] = data_day.apply(lambda row: f"{row['yr']}_{row['mnth']}", axis=1) 

# Data hari
data_day['day_of_week'] = data_day['dteday'].dt.day_name()
rataPengguna = data_day.groupby('day_of_week')['cnt'].mean()
hari = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
rataPengguna = rataPengguna.reindex(hari)

# Mendefinisikan waktu dari Pagi, Siang, Sore, dan Malam
w_pagi = data_hour[(data_hour['hr'] >= 6) & (data_hour['hr'] < 12)]
w_siang = data_hour[(data_hour['hr'] >= 12) & (data_hour['hr'] < 18)]
w_sore = data_hour[(data_hour['hr'] >= 18) & (data_hour['hr'] < 22)]
w_malam = data_hour[(data_hour['hr'] >= 22) & (data_hour['hr'] < 0)]
w_tengah_malam = data_hour[(data_hour['hr'] >= 0) & (data_hour['hr'] < 6)]

if selected == "Home":
    st.subheader(f"Halaman {selected}")
    st.title("Kelompok 6")
    st.markdown("<h3>Anggota Kelompok :</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>- 10123001 Hadi Rabani</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>- 10123006 Sendi Dwi Putra</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>- 10123008 Dandy Muhamad Fadillah</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>- 10123021 Irfan Putra Hendari</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>- 10123023 Dinda Aprillianti</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>- 10123026 Egy Audiawan Riyadi</p>", unsafe_allow_html=True)
    st.markdown("<h3>Penjelasan Menu :</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='font-size: 20px;'>- Menu 1 Dibuat Oleh Hadi Rabani</h5>", unsafe_allow_html=True)
    st.write('Penggunaan Sepeda Sepanjang Tahun 2011')
    st.markdown("<p style='font-size: 20px;'>- Menu 2 Dibuat Oleh Sendi Dwi Putra", unsafe_allow_html=True)
    st.write('Penggunaan Sepeda Berdasarkan jam')
    st.markdown("<p style='font-size: 20px;'>- Menu 3 Dibuat Oleh Dandy Muhamad Fadillah", unsafe_allow_html=True)
    st.write('Penggunaan Sepeda Berdasarkan Waktu Pagi, Siang dan Sore')
    st.markdown("<p style='font-size: 20px;'>- Menu 4 Dibuat Oleh Irfan Putra Hendari", unsafe_allow_html=True)
    st.write('Penggunaan Sepeda Berdasarkan per Hari dalam Seminggu')
    st.markdown("<p style='font-size: 20px;'>- Menu 5 Dibuat Oleh Dinda Aprillianti", unsafe_allow_html=True)
    st.write('Penyewaan Sepeda Berdasarkan Musim')
    st.markdown("<p style='font-size: 20px;'>- Menu 6 Dibuat Oleh Egy Audiawan Riyadi", unsafe_allow_html=True)
    st.write('Penyewaan Sepeda Berdasarkan Cuaca') 

elif selected == "Menu 1": # Penggunaan Sepeda Sepanjang Tahun 2011

    st.subheader('Penggunaan Sepeda Sepanjang Tahun 2011')

    # Pastikan kolom tanggal dalam format datetime
    data_day["dteday"] = pd.to_datetime(data_day["dteday"])
    
    # Kolom untuk sorting (format 'YYYY-MM')
    data_day['yr_month'] = data_day['dteday'].dt.strftime('%Y-%m')
    
    # Tambahkan kolom baru untuk label tahun dan bulan dalam bahasa Indonesia
    data_day["year_month_label"] = data_day["dteday"].dt.strftime("%Y %B")  # Contoh: "2011 Januari"
    
    # Urutkan data berdasarkan 'yr_month' agar sumbu X berurutan
    data_day = data_day.sort_values(by='yr_month')
    
    # Pastikan label sumbu X memiliki urutan yang benar
    ordered_months = [
        '2011 Jan', '2011 Feb', '2011 Mar', '2011 Apr', '2011 Mei', '2011 Jun', 
        '2011 Jul', '2011 Agu', '2011 Sep', '2011 Okt', '2011 Nov', '2011 Des',
        '2012 Jan', '2012 Feb', '2012 Mar', '2012 Apr', '2012 Mei', '2012 Jun',
        '2012 Jul', '2012 Agu', '2012 Sep', '2012 Okt', '2012 Nov', '2012 Des'
    ]

    # Membuat grafik dengan Altair
    chart = alt.Chart(data_day).mark_line().encode(
        x=alt.X('year_month_label:N', 
                title='Tahun dan Bulan', 
                sort=ordered_months,  # Pastikan urutan bulan benar
                axis=alt.Axis(labelAngle=90)),  # Rotasi label sumbu X agar terbaca jelas
        y=alt.Y('cnt:Q', title='Jumlah Penggunaan Sepeda'),
        tooltip=['year_month_label', 'cnt']
    ).properties(
        title='Penggunaan Sepeda Sepanjang Tahun 2011 hingga 2012',
        width=800,
        height=400
    )
    # Menampilkan grafik di Streamlit
    st.altair_chart(chart, use_container_width=True)

    # Penjelasan untuk Penggunaan Sepeda sepanjang tahun 2011
    st.write("Penjelasan: Grafik ini menunjukkan jumlah penggunaan sepeda sepanjang tahun 2011 dan bulanannya. "
            "Dari data yang ditampilkan, kita dapat melihat bahwa penggunaan sepeda paling tinggi pada bulan Maret tahun 2012.")

elif selected == "Menu 2": # Penggunaan Sepeda Berdasarkan Jam
    
    st.subheader('Penggunaan Sepeda Berdasarkan Jam')
    data_perjam = data_hour.groupby('hr')['cnt'].mean().reset_index()

    # Menampilkan Line Chart menggunakan Streamlit
    st.line_chart(data_perjam.set_index('hr')['cnt'])

    # Penjelasan untuk Penggunaan Sepeda sepanjang Jam
    st.write("penjelasan: Grafik ini menunjukkan rata-rata jumlah penggunaan sepeda berdasarkan jam. "
            "Dari data yang ditampilkan, kita dapat melihat bahwa penggunaan sepeda paling tinggi pada jam 5 sore.")

elif selected == "Menu 3":  # Pengguna Sepeda Berdasarkan Waktu Pagi, Siang, Sore
    
    st.subheader('Pengguna Sepeda Berdasarkan Waktu Pagi, Siang, Sore')
    # Menambahkan kategori waktu: Pagi, Siang, Sore, Malam
    def categorize_time(hour):
        if 5 <= hour < 10:
            return 'Pagi'
        elif 10 <= hour < 15:
            return 'Siang'
        elif 15 <= hour < 18:
            return 'Sore'
        else:
            return 'Malam'

    # Menambahkan kolom waktu berdasarkan jam (hr)
    data_hour['waktu'] = data_hour['hr'].apply(categorize_time)

    # Menggabungkan data yang sudah ada dengan kategori waktu
    data_waktu = data_hour[['hr', 'cnt', 'waktu']]

    # Membuat grafik menggunakan Altair
    chart = alt.Chart(data_waktu).mark_line().encode(
        x=alt.X('hr:O', title='Jam'),
        y=alt.Y('cnt:Q', title='Jumlah Penggunaan Sepeda'),
        color='waktu:N',  # Menandakan warna berdasarkan kategori waktu
        tooltip=['hr', 'cnt', 'waktu']
    ).properties(
        title="Penggunaan Sepeda Berdasarkan Waktu Pagi, Siang, Sore, Malam"
    )

    # Menampilkan chart di Streamlit
    st.altair_chart(chart, use_container_width=True)

    # Penjelasan untuk Penggunaan Sepeda berdasarkan waktu Pagi, Siang, Sore
    st.write("Penjelasan: Grafik ini menunjukan jumlah penggunaan sepeda berdasarkan waktu pagi, siang, sore, dan malam. "
            "Dari data yang ditampilkan, kita dapat melihat bahwa penggunaan sepeda paling tinggi pada Sore dan Malam.")

elif selected == "Menu 4": # Penggunaan Sepeda Per Hari dalam Seminggu
    
    st.subheader('Penggunaan Sepeda Per Hari dalam Seminggu')
    # Menambahkan kolom untuk hari dalam seminggu
    data_day['day_of_week'] = pd.to_datetime(data_day['dteday']).dt.day_name()

    # Menghitung rata-rata penggunaan sepeda berdasarkan hari dalam seminggu
    rataPengguna = data_day.groupby('day_of_week')['cnt'].mean()
    hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    rataPengguna = rataPengguna.reindex(hari)

    # Menyiapkan data untuk grafik
    data_perhari = data_day.groupby('weekday')['cnt'].sum().reset_index()
    data_perhari['weekday'] = data_perhari['weekday'].map({0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'})

    # Mengatur urutan hari dalam seminggu
    from pandas.api.types import CategoricalDtype
    day_order = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    data_perhari['weekday'] = pd.Categorical(data_perhari['weekday'], categories=day_order, ordered=True)

    # Menyiapkan data untuk streamlit bar_chart
    source = data_perhari[['weekday', 'cnt']]

    # Membuat grafik menggunakan Streamlit
    st.bar_chart(source.set_index('weekday')['cnt'])

    # Penjelasan untuk Penggunaan Sepeda per Hari dalam Seminggu
    st.write("Penjelasan: Grafik ini menunjukkan jumlah penggunaan sepeda per hari dalam seminggu. "
            "Dari data yang ditampilkan, kita dapat melihat bahwa penggunaan sepeda paling tinggi pada hari Jumat dan Sabtu")

elif selected == "Menu 5": # Penyewaan Sepeda Berdasarkan Musim

    st.subheader('Penyewaan Sepeda Berdasarkan Musim')
    
    # Mengelompokkan data berdasarkan musim dan jumlah penyewaan sepeda
    data_musim = data_day.groupby('season')['cnt'].sum().reset_index()
    data_musim = data_musim[data_musim['season'].isin([1, 2, 3, 4])]
    # Label Musim
    musim_labels = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
    data_musim['season_label'] = pd.Categorical(data_musim['season'], categories=[1, 2, 3, 4], ordered=True)
    data_musim['season_label'] = data_musim['season_label'].map(dict(zip([1, 2, 3, 4], musim_labels)))

    chart = alt.Chart(data_musim).mark_bar().encode(
        x=alt.X('season_label:N', title='Musim', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('cnt:Q', title='Jumlah Penyewaan Sepeda'),
        color=alt.Color('season:N', scale=alt.Scale(domain=[1, 2, 3, 4], range=['#6c3c0c','#ff7f0e', '#2ca02c', '#d62728']), legend=None)
    ).properties(
        width=500,
        height=300,
        title="Jumlah Penyewaan Sepeda Berdasarkan Musim"
    )

    st.altair_chart(chart, use_container_width=True)

    # Penjelasan untuk Penyewaan Sepeda berdasarkan Musim
    st.write("Penjelasan: Grafik ini menunjukkan jumlah penyewaan sepeda berdasarkan musim. "
            "Dari data yang ditampilkan, kita dapat melihat tren penggunaan sepeda di setiap musim paling tinggi pada Musim Gugur.")

elif selected == "Menu 6": # Penyewaan Sepeda Berdasarkan Cuaca

    st.subheader('Penyewaan Sepeda Berdasarkan Cuaca')

    # Mapping Kondisi Cuaca
    weather_mapping = {
        1: 'Cuaca Baik',
        2: 'Cuaca Buruk',
        3: 'Cuaca Tidak Diketahui'
    }

    data_cuaca = data_day.groupby('weathersit')['cnt'].sum().reset_index()

    # Mengganti Angka dengan Label
    data_cuaca['weathersit'] = data_cuaca['weathersit'].map(weather_mapping)

    chart_cuaca = alt.Chart(data_cuaca).mark_bar().encode(
        x=alt.X('weathersit:N', title='Kondisi Cuaca',axis=alt.Axis(labelAngle=0)),
        y=alt.Y('cnt:Q', title='Jumlah Penyewaan Sepeda'),
        color=alt.Color('weathersit:N', scale=alt.Scale(scheme='set2'), title='Kondisi Cuaca'),
        tooltip=['weathersit', 'cnt']
    )

    st.altair_chart(chart_cuaca, use_container_width=True)

    # Penjelasan untuk Penyewaan Sepeda berdasarkan Cuaca
    st.write(
        "Penjelasan: Grafik ini menunjukkan jumlah penyewaan sepeda berdasarkan cuaca. "
        "Dari data yang ditampilkan, kita dapat melihat bahwa penyewaan sepeda lebih banyak terjadi "
        "pada cuaca yang baik dibandingkan cuaca buruk, dan terdapat data yang tidak diketahui mengenai cuaca."
    )

elif selected == "Menu 7":  # Menu untuk unggah file CSV
    
    st.subheader('Upload File CSV')

    # Menggunakan file uploader untuk mengunggah file CSV
    file1 = st.file_uploader('Unggah File CSV', type='csv')

    # Menggunakan file uploader kedua untuk mengunggah file CSV kedua
    #file2 = st.file_uploader('Unggah File CSV Kedua', type='csv')

    if file1 is not None:
        # Membaca file CSV yang diunggah
        data = pd.read_csv(accept_multiple_files=True, file)
        
        # Menampilkan dataframe
        st.write('Isi Dari Data Frame Adalah:')
        st.dataframe(data)
        
        # Membuat visualisasi menggunakan Altair (contoh: bar chart)
        if 'x_column' in data.columns and 'y_column' in data.columns:
            chart = alt.Chart(data).mark_bar().encode(
                x='x_column:N',
                y='y_column:Q'
            ).properties(
                title='Visualisasi Data Berdasarkan File CSV'
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.write("Kolom yang dibutuhkan tidak ditemukan dalam data.")

    # Jika file kedua diunggah
    #if file2 is not None:
     #   data2 = pd.read_csv(file2)
      #  st.write('Isi Dari Data Frame CSV Kedua Adalah:')
       # st.dataframe(data2)

        # Visualisasi untuk file kedua
        #if 'x_column' in data2.columns and 'y_column' in data2.columns:
         #   chart2 = alt.Chart(data2).mark_bar().encode(
          #      x='x_column:N',
           #     y='y_column:Q'
            #).properties(
             #   title='Visualisasi Data Berdasarkan File CSV Kedua'
            #)
            #st.altair_chart(chart2, use_container_width=True)
        #else:
         #   st.write("Kolom yang dibutuhkan tidak ditemukan dalam file kedua.")
