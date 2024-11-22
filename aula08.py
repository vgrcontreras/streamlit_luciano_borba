import random

import numpy as np
import pandas as pd
import streamlit as st

data = {
    'dia': range(1, 31),
    'vendas': np.random.randint(low=100, high=300, size=30 )
}

df = pd.DataFrame(data)

st.line_chart(df, x='dia', y='vendas')

data = {
    'vendedor': ['victor', 'giovana', 'julia'],
    'vendas': [30, 50, 20]
}

df2 = pd.DataFrame(data)

st.bar_chart(df2, x='vendedor', y='vendas')