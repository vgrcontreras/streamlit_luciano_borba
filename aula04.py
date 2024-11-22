import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Aula 04'
)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Score': [85.5, 90.2, 88.0, 76.3]
}

df = pd.DataFrame(data)

st.write('Dataframe')
st.dataframe(df)

st.write('Tabela')
st.table(df)

# print(df)