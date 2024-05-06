import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

dados = pd.read_csv('venv\estoque.csv')

st.title('Toma gap :sunglasses:\n')
st.write('Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria, de uma base de dados de produtos de supermercado')

checkbox_mostar_tabela = st.sidebar.checkbox('Mostrar tabela')
if checkbox_mostar_tabela:
    st.sidebar.markdown('## Filtro para a tabela')

    categorias = list(dados['Categoria'].unique())
    categorias.append('Todas')

    categoria = st.sidebar.selectbox("Selecione a categoria para apresentar na tabela", options = categorias)

    def mostra_qntd_linhas(dataframe):

        qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 1, max_value = len(dataframe), step = 1)

        st.write(dataframe.head(qntd_linhas).style.format(subset = ['Valor'], formatter="{:.2f}"))

    if categoria != 'Todas':
        df_categoria = dados.query('Categoria == @categoria')
        mostra_qntd_linhas(df_categoria)
    else:
        mostra_qntd_linhas(dados)


