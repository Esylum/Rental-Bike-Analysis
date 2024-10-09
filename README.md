## Bike Rentals - Final Project Data Analytics 
Ini adalah tugas akhir dari Dicoding untuk kursus “Belajar Analisis Data Dengan Python”, yang bertujuan untuk menganalisis dan membuat dasbor dari dataset bike sharing. Dalam file buku catatan, saya menyertakan langkah-langkah yang saya ambil untuk analisis, yang meliputi Data Wrangling, Analisis Data Eksplorasi, dan Visualisasi Data. Selain itu, saya membuat dasbor menggunakan Streamlit, yang dapat Anda akses dengan mengeklik tautan di bilah sisi kanan or [here]([https://bike-sharing-rentals-dicoding-final-project-yyw4s7kdygiumzfwtw.streamlit.app/](https://rental-bike-analysis-bwarzxylrupjtwvk9mfmou.streamlit.app/)).

Untuk informasi lebih lanjut, seperti latar belakang dataset ini, karakteristik
karakteristiknya, struktur file, dan banyak lagi, silakan lihat file Readme
file Readme. Oleh karena itu, saya tidak akan menguraikan lebih lanjut di sini.

1. File Structure
```
    ├───Dashboard
    | ├───Esylum Rent.png
    | ├───dashboard.py
    | └───day.csv
    | └───hour.csv
    ├───Bike-sharing-dataset
    | ├───Readme.txt
    | ├───day.csv
    | └───hour.csv
    ├───screenshots
    | ├───Rental Dashboard & Monthly Rentals.png
    | ├───Seasonly Rentals.png
    | └───Weatherly Rentals.png
    | └───Weekday, Working Day, and Holiday Rentals.png
    ├───Data_Project_Analysis_Bike_Sharing_Dataset.ipynb
    ├───Data_Project_Analysis_Bike_Sharing_Dataset.py
    ├───README.md
    └───requirements.txt
```

2. Siklus kerja proyek
    1. Penguraian Data:
        - Mengumpulkan data
        - Menilai data
        - Membersihkan data
    2. Analisis Data Eksplorasi:
        - Menentukan pertanyaan bisnis untuk eksplorasi data
        - Membuat eksplorasi data
    3. Visualisasi Data:
        - Membuat Visualisasi Data yang menjawab pertanyaan bisnis 
    4. Dasbor: 
        - Mengatur DataFrame yang akan digunakan
        - Membuat komponen-komponen filter pada dashboard 
        - Lengkapi dashboard dengan berbagai visualisasi data

3. Memulai
Rent_Data_Analysis.ipynb
 1. Unduh proyek ini.
 2. Buka IDE favorit Anda seperti Jupyter Notebook atau Google Colaboratory (tapi di sini saya akan menggunakan Google Colab). 
 3. Buatlah sebuah Notebook Baru.
 4. Unggah dan pilih file dengan ekstensi .ipynb.
 5. Sambungkan ke runtime yang dihosting.
 6. Terakhir, jalankan sel kode.

Dasbor/dashboard.py 
 1. Unduh proyek ini.
 2. Instal Streamlit di terminal atau prompt perintah Anda menggunakan pip install streamlit. Instal pustaka-pustaka lain seperti pandas, numpy, scipy,
matplotlib, dan seaborn jika Anda belum melakukannya.
 3. Harap diperhatikan, jangan memindahkan berkas csv karena ia bertindak sebagai sumber data. simpan dalam satu folder sebagai
dashboard.py
 4. Buka VSCode Anda dan jalankan berkas tersebut dengan mengeklik tombol
terminal dan tuliskan streamlit run dashboard.py.
