import streamlit as st

#App With Streamlit
# Judul aplikasi
st.title("📊 Aplikasi Sentimen Analisis")

# Deskripsi aplikasi
st.write(
    "Selamat datang di aplikasi sentimen analisis!"
)
st.write(
    "Karya Leonard Agust Laga Lajar"
)
st.write(
    "Untuk melakukan sentimen analisis, silahkan masukkan teks."
)

# Input teks dari pengguna
user_input = st.text_area("Masukkan teks untuk analisis sentimen:")

# Menampilkan hasil prediksi
# Naive Bayes
st.subheader("1. Naive Bayes")
st.write(f"Prediksi Naive Bayes: belum ada data")

# KNN
st.subheader("2. KNN")
st.write(f"KNN Prediction: belum ada data")

# SVM
st.subheader("3. SVM")
st.write(f"SVM Prediction: belum ada data")