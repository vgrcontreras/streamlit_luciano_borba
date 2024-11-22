import pandas as pd
import streamlit as st

## selectbox

select_box = st.selectbox(
    label='Selecione sua cor favorita:',
    options=('Azul', 'Vemelhor', 'Verde')
)

## multiselect

multi_select_box = st.multiselect(
    label='Selecione sua(s) cor(es) favorita(s)',
    options=('Azul', 'Vermelho', 'Verde', 'Amarelo')
)

st.write(f'As suas cores favoritas são: {multi_select_box}')

## file_upload

file = st.file_uploader('Suba seu arquivo excel', type='xlsx')

if file:
    dataframe = pd.read_excel(file)
    st.dataframe(dataframe)

