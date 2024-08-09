# streamlit run Streamlit_Acoes_2024.py
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

# Cotações


@st.cache_data
def carregar_dados(empresas):
    texto_tickers = ' '.join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period='1d', start='2010-01-01', end='2024-08-05')
    cotacoes_acao = cotacoes_acao['Close']
    return cotacoes_acao


acoes = ['ITUB4.SA', 'PETR4.SA', 'MGLU3.SA', 'VALE3.SA', 'ABEV3.SA', 'WEGE3.SA']
dados = carregar_dados(acoes)

# print(dados)

# Interface
st.write('''
# Preço de Ações 
O gráfico representa as ações ao longo dos anos   
''')

# filtros sidebar
st.sidebar.header('Filtros')


# filtros de ações
lista_acoes = st.sidebar.multiselect('Escolha as ações', dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Adj Close"})

# filtro data
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider('Selecione o período', 
                                     min_value=data_inicial, 
                                     max_value=data_final,
                                     value=(data_inicial, data_final),
                                    step=timedelta(days=1))

dados = dados.loc[intervalo_data[0]:intervalo_data[1]]

# Gráfico
st.line_chart(dados)
