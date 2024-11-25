from datetime import datetime

import streamlit as st

st.title('Opções de Input com Streamlit')

st.divider()
nome = st.text_input('Coloque seu Nome:')
description = st.text_area('Decreva quem você é:', max_chars=500)
age = st.number_input(
    label='Coloque sua idade:',
    min_value=18,
    max_value=100
)
dt_nascimento = st.date_input(
    'Coloque sua data de nascimento:',
    min_value=datetime(1900,1,1)
)
hr_agendamento = st.time_input('Indique a hora que deseja agendar')
slider = st.slider(
    label='Selecione um valor entre 0 e 100',
    min_value=0,
    max_value=100,
    value=25
)