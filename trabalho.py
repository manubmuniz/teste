import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Gráfico de Barras Simples")

    # Criando alguns dados fictícios
    data = pd.DataFrame({
        'Categoria': ['A', 'B', 'C', 'D'],
        'Valor': [10, 20, 15, 25]
    })

    # Plotando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(data['Categoria'], data['Valor'])
    ax.set_xlabel('Categoria')
    ax.set_ylabel('Valor')
    ax.set_title('Gráfico de Barras')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
