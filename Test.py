import streamlit as st

st.header('Aplikasi Penjumlahan Bilangan Numerik', divider = 'rainbow')

angka_pertama = st.number_input('Masukkan Angka pertama')
st.write('Angka pertama adalah',angka_pertama)

angka_kedua = st.number_input('Masukkan Angka kedua')
st.write('Angka kedua adalah',angka_kedua)

operasi_matematika_pertambahan = angka_pertama+angka_kedua
operasi_matematika_pengurangan = angka_pertama-angka_kedua
operasi_matematika_perkalian = angka_pertama*angka_kedua
operasi_matematika_pembagian = angka_pertama/angka_kedua

st.write(f"Angka pertama {angka_pertama} + Angka kedua {angka_kedua} = {operasi_matematika_pertambahan}")
st.write(f"Angka pertama {angka_pertama} - Angka kedua {angka_kedua} = {operasi_matematika_pengurangan}")
st.write(f"Angka pertama {angka_pertama} / Angka kedua {angka_kedua} = {operasi_matematika_pembagian}")
st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua} = {operasi_matematika_perkalian}")

st.image("https://res.cloudinary.com/dk0z4ums3/image/upload/v1627618536/attached_image/mengingatkan-kembali-kepada-manfaat-karbohidrat.jpg", width=300)
