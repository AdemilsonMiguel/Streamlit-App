import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ações Tesla")

with st.container():
    st.subheader("Site com o Streamlit")
    st.title("Dashboard de Ações")
    st.write("Informações sobre as ações da Tesla")


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("tsla_2023.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Date", y="Close")

