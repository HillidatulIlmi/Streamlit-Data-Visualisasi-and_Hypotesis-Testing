import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px
import streamlit as st

@st.cache
def load_data():
    data = pd.read_csv('h8dsft_Milestone1_HillidatulIlmi_user & inventory_Items.csv')
    return data

def app():
    df = load_data()

    st.title('Diagram Batang Pembelian Barang Inventaris Beberapa Negara')
    fig1, ax1 = plt.subplots()
    sns.countplot(df['country'],ax=ax1)
    st.pyplot(fig1)

    st.title('Hubungan Usis Pelangan dengan Harga barang inventaris')
    fig2, ax2 = plt.subplots()
    sns.scatterplot(df['age'],df['product_retail_price'],ax=ax2)
    st.pyplot(fig2)

    st.title('Grafik Pie Kategori Barang Inventaris')
    labels =(df['product_category']).value_counts()
    fig3, ax3 = plt.subplots()
    ax3.pie(labels, autopct="%1.1f%%")
    ax3.axis("equal")
    st.pyplot(fig3)

    st.title('Grafik Pie Gender Yang Melakukan Transaksi Barang Inventaris')
    gender =(df['gender']).value_counts()
    fig4, ax4 = plt.subplots()
    ax4.pie(gender, autopct="%1.1f%%")
    ax4.axis("equal")
    st.pyplot(fig4)