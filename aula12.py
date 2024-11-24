import streamlit as st

st.title('Vivi ama Juju')

st.divider()

with st.expander('Sobre mim:'):
    st.divider()
    nome = st.text_input('Nome:')
    idade = st.number_input('Idade:')
    genero = st.selectbox(
        label='Genero:',
        options=('Masculino', 'Feminino')
    )