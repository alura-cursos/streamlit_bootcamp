import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
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

    #plt.figure(figsize=(8, 6))
    return sns.barplot(x="Ano", y="Total", data=dados)
    #plt.title(f"Óbitos por {causa} - {estado}")
    # plt.show()


def main():

    obitos_2019 = carrega_dados("dados/obitos-2019.csv")
    obitos_2020 = carrega_dados("dados/obitos-2020.csv")
    figura = grafico_comparativo(obitos_2019, obitos_2020,
                                 "SRAG")

    st.title("Análise de Óbitos 2019-2020")
    st.markdown("Este trabalho analisa dados dos **óbitos 2019-2020**")

    st.pyplot(figura)


if __name__ == "__main__":
    main()
