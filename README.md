# **Submission Dicoding: Belajar Data Analytics dengan Python**  

## 📊 **Project Data Analytics**  
 Proyek ini berfokus pada analisis *E-Commerce Public Dataset*. Dalam proyek ini, saya melakukan analisis mendalam terhadap data e-commerce dengan tujuan menemukan pola, tren, serta wawasan yang dapat dimanfaatkan untuk pengambilan keputusan berbasis data.  

## 📂 **Struktur Direktori**  
 
Berikut adalah struktur direktori:

```
📂 Proyek_Analisis_Data_E_CommercePublicDataset  
│── 📄 Proyek_Analisis_Data_E_CommercePublicDataset.ipynb  # Notebook Jupyter untuk eksplorasi dan analisis data  
│── 📄 README.md                                           # Dokumentasi proyek  
│── 📄 requirements.txt                                    # Daftar pustaka yang diperlukan untuk menjalankan proyek  
│── 📄 url.txt                                             # File berisi daftar URL terkait proyek  
│  
├── 📁 dashboard                                        # Folder untuk Dashboard Streamlit.app  
│   ├── 📄 dashboard.py                                 # Script utama untuk menjalankan dashboard  
│   ├── 📄 func.py                                      # Fungsi tambahan untuk analisis data dalam dashboard  
│   ├── 📄 geolocation.csv                              # Dataset geolokasi pelanggan untuk visualisasi  
│   ├── 📄 logo.jpg                                     # Logo yang digunakan dalam tampilan dashboard 
│   ├── 📄 ss.jpg                                       # Screenshot tampilan dashboard setelah dijalankan 
│   ├── 📄 main_data.csv                                # Dataset utama yang digunakan dalam dashboard  
│   │  
│   ├── 📁 dashboard                                    # Duplikat dataset agar tidak error saat dijalankan di lokal  
│   │   ├── 📄 geolocation.csv  
│   │   ├── 📄 logo.jpg  
│   │   ├── 📄 main_data.csv  
│   │  
│   ├── 📁 __pycache__                                 # Folder cache Python untuk mempercepat eksekusi kode  
│       ├── 📄 func.cpython-312.pyc  
│       ├── 📄 func.cpython-39.pyc  
│  
└── 📁 dataset e-commerce                             # Folder dataset mentah yang digunakan dalam analisis  
    ├── 📄 customers_dataset.csv                      # Data pelanggan e-commerce  
    ├── 📄 geolocation_dataset.csv                    # Data geolokasi pelanggan dan penjual  
    ├── 📄 orders_dataset.csv                         # Informasi pesanan pelanggan  
    ├── 📄 order_items_dataset.csv                    # Detail barang dalam setiap pesanan  
    ├── 📄 order_payments_dataset.csv                 # Informasi pembayaran pelanggan  
    ├── 📄 order_reviews_dataset.csv                  # Data ulasan pelanggan  
    ├── 📄 products_dataset.csv                       # Informasi produk e-commerce  
    ├── 📄 product_category_name_translation.csv      # Terjemahan kategori produk  
    ├── 📄 sellers_dataset.csv                        # Informasi penjual e-commerce  
```
 

## ⚙ **Instalasi**  
Jalankan perintah berikut untuk mengunduh repository ke komputer lokal:  

### **1️⃣ Download atau Clone Repository**  
```bash
git clone https://github.com/johanadis/Proyek_Analisis_Data_E-CommercePublicDataset.git
```

### **2️⃣ Buat Environment Baru dengan Python 3.9**  
Gunakan **conda** untuk membuat environment baru:  
```bash
conda create --name ds python=3.9  
```

### **3️⃣ Aktifkan Environment**  
Setelah environment berhasil dibuat, aktifkan dengan perintah:  
```bash
conda activate ds  
```

### **4️⃣ Install Dependensi yang Dibutuhkan**  
Instal pustaka yang diperlukan untuk analisis data dan visualisasi:  
```bash
pip install matplotlib seaborn pandas streamlit numpy
```
Atau, bisa jalankan code di bawah ini (pilih salah satu):
```bash
pip install -r requirements.txt
```

Sekarang lingkungan pengembanganmu sudah siap! 🚀  

## 🎯 **Menjalankan Aplikasi Streamlit**  
Setelah setup selesai, jalankan aplikasi dashboard dengan perintah berikut:  

```bash
cd dashboard
streamlit run dashboard.py  
```  
Atau bisa dengan kunjungi website ini [Project Data Analytics E-CommercePublicDataset](https://e-commerce-johanadi.streamlit.app/)

<img src="./dashboard/ss.png" alt="SS Streamlit App"></img>

✨ **Dashboard interaktif Anda siap digunakan!** 🎉  



## 🙏 **Terima Kasih** 😊
