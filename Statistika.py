import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px
import streamlit as st

@st.cache
def variabel():
    data = pd.read_csv('h8dsft_Milestone1_HillidatulIlmi_orderitems & product.csv')
    return data

def app():
    dt = variabel()
    dt['SaleOrderan'] = dt['sale_price']#variabel data income berisikan data quantity control pada barang unitprice
    dt['date'] = dt['created_at']#variabel data berisikan tahun dilakukannya produksi
    Potongan_Harga = dt[['date','SaleOrderan']].groupby('date').sum() 
    ratarata = format(np.round(Potongan_Harga['SaleOrderan'].mean()))
    st.subheader('ONE SAMPLE T-TEST ONE TAILED')
    st.write(dt)
    st.write('Pengujian one sampel t-test one tailed digunakan untuk melihat ada atau tidaknya signifikan peningkatan potongan harga produk di toko The Look.')
    st.write('1. Mencari nilai Rata-rata potongan harga produk')
    st.write('Setelah dilakukan perhitungan diperoleh bahwa rata-rata potongan harga pada produk yang di jual toko The Look adalah')
    st.write("Rata-rata potongan harga :",ratarata)
    st.write('2. Untuk memeriksa apakah harga potongan kepada pelanggan toko the look meningkat secara signifikan atau tidak, akan melakukan sampel tunggal satu sisi dan menetapkan tingkat signifikansi 0,05. Kami menggunakan metode ini karena kami hanya menguji variabel dan membandingkan sampel (data harga potongan ynag sering dipakai yaitu 25 dolar) dan populasi (kami menganggap itu adalah data harga potongan beberapa hari terakhir ini).')
    st.write('HIPOTSIS')
    st.write('**H0: μ <= \$59**')
    st.write('**H1: μ > \$59**')
    st.write('Berikut nilai p-value dan t-statistics')
    t_stat,p_val = stats.ttest_1samp(Potongan_Harga.SaleOrderan,25)
    Pvalue = p_val/2
    T = t_stat
    st.write("Nilai P-value :",Pvalue)
    st.write("Nilai t-statistics :",T)
    st.write('Hasil 0,0 lebih kecil dari 0,05 maka dengan ini menolak h0. yang artinya ada perbedaan signifikan beberapa harga potongan terhadap produk akhir-akhir ini di toko the look.')
    st.write('3. Berdasarkan pengujian One sample one tailed, diperoleh bahwa terjadi perubahan signifikan mengenai potongan harga pada produk yang di jual toko the look. Berdasarkan hal ini CEO the look bisa mempertahankan harga potogan produk sehingga akan makin banyak pelangan yang berminat melakukan transaksi.')


