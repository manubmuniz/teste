import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Gráfico de Contagem de Níveis de Experiência")

    df = pd.read_csv('ds_salaries.csv')

    if 'experience_level' not in df.columns:
        st.error("O arquivo CSV não contém a coluna 'experience_level'.")
        return

    experience_counts = df['experience_level'].value_counts()

    colors = ['skyblue', 'pink', 'yellow', 'orange']

    fig, ax = plt.subplots()
    experience_counts.plot(kind='bar', ax=ax, color=colors)
    ax.set_xlabel('Nível de Experiência')
    ax.set_ylabel('Contagem')
    ax.set_title('Contagem de Níveis de Experiência')

    st.pyplot(fig)

if __name__ == "__main__":
    main()

