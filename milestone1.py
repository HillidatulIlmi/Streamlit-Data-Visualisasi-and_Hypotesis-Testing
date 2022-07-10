import DataVisualisasi, Statistika
import streamlit as st

PAGES = {'Data Visualization': DataVisualisasi,
         'Statistical Analysis':Statistika}

selected = st.sidebar.radio('Select Page: ', ['Data Visualization', 'Statistical Analysis'])

page = PAGES[selected]

page.app()