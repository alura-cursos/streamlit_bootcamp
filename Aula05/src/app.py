import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from time import sleep


@st.cache
def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    sleep(3)
    return dados


def grafico_comparativo(dados_2019, dados_2020, causa, estado="BRASIL"):

    if estado == "BRASIL":
        total_2019 = dados_2019.groupby("tipo_doenca").sum()
        total_2020 = dados_2020.groupby("tipo_doenca").sum()
        lista = [int(total_2019.loc[causa]), int(total_2020.loc[causa])]

    else:
        total_2019 = dados_2019.groupby(["uf", "tipo_doenca"]).sum()
        total_2020 = dados_2020.groupby(["uf", "tipo_doenca"]).sum()
        lista = [int(total_2019.loc[estado, causa]),
                 int(total_2020.loc[estado, causa])]
    dados = pd.DataFrame({"Total": lista,
                          "Ano": [2019, 2020]})

    fig, ax = plt.subplots()
    ax = sns.barplot(x="Ano", y="Total", data=dados)
    ax.set_title(f"Óbitos por {causa} = {estado}")

    return fig


def main():

    obitos_2019 = carrega_dados("dados/obitos-2019.csv")
    obitos_2020 = carrega_dados("dados/obitos-2020.csv")
    tipo_doenca = obitos_2020["tipo_doenca"].unique()
    estado = np.append(obitos_2020["uf"].unique(), "BRASIL")

    st.title("Análise de Óbitos 2019-2020")
    st.markdown("Este trabalho analisa dados dos **óbitos 2019-2020**")

    opcao_1 = st.sidebar.selectbox("Selecione o tipo doença",
                                   tipo_doenca)

    opcao_2 = st.sidebar.selectbox("Selecione o Estado", estado)

    figura = grafico_comparativo(obitos_2019, obitos_2020,
                                 opcao_1, opcao_2)

    st.pyplot(figura)


if __name__ == "__main__":
    main()
