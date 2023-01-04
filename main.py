import streamlit as st
from making_predictions import make_prediction


st.title('Klasifikasi Sentimen dari Ulasan Produk')
st.write('Ayo cari tahu sentimen dari ulasan produk anda dengan lebih cepat! Positif, Negatif atau Netral ya???')


contoh_teks = st.selectbox(
    'Contoh teks review / ulasan produk: ',
    ('Cukup sepadan untuk harga segini, lumayan lah', 'Barang ini sangat sesuai dengan harganya, mantap', 'kualitas barang ini kurang baik. Sangat mengecewakan.'))

if contoh_teks != None:
    hasil = make_prediction(contoh_teks)
    st.write(f"Sentimen dari '{contoh_teks}' adalah: {str(hasil['MLP prediction'][0])}",
             )
else:
    print('Maaf, ada masalah')

st.subheader('Masukkan :blue[ulasan] yang ada peroleh ke bawah:')

ulasan = st.text_area('Teks Ulasan:', )

if st.button('Prediksi Sentimen'):
    hasil = make_prediction(contoh_teks)
    st.write(f"Sentimen dari '{ulasan}' adalah: :blue[{str(hasil['MLP prediction'][0])}]",
             )

else:
    st.write('Belum ada ulasan yang masuk')

# if ulasan != None:
#     hasil = make_prediction(contoh_teks)
#     st.write(f"Sentimen dari '{ulasan}' adalah: {str(hasil['MLP prediction'][0])}",
#              )
# else:
#     print('Belum ada ulasan yang masuk')
