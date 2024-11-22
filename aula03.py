import streamlit as st

st.header('Aula 3 - Checkbox, Radio e botões')
st.subheader('Com Luciano Borba')

banho = st.checkbox('Tomar banho')
escovar_dentes = st.checkbox('Escovar dentes')

opinion = st.button('Opinião')

if opinion:
    if banho and escovar_dentes:
        st.success('Você está de banho tomado e dentes escovados')
    elif banho and not escovar_dentes:
        st.warning('Você está de banho tomado mas precisa escovar os dentes')
    elif not banho and escovar_dentes:
        st.warning('Você escovou os dentes mas precisa tomar banho!!')
    else:
        st.error('Você é um PORCO!!!!')


radio = st.radio('Qual a cor favorita do Victor:',
                 options=['Verde', 'Vermelho', 'Amarelo', 'Azul'])

responder = st.button('Responder')

if responder:
    if radio == 'Azul':
        st.success('Você acertou!')
    else: 
        st.warning('Você errou!')

