
import pandas as pd
import plotly.express as px
import streamlit as st

# Agregar una sección para subir el archivo
st.title('Codon Visualizer')
uploaded_file = st.file_uploader('Subir archivo', type='xlsx')

# Comprobar si se ha subido el archivo y leer el archivo
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    genes = df['Gen'].unique().tolist()
    
    # Agregar una sección para que el usuario seleccione el gen que desea visualizar
    gene = st.selectbox('¿Qué gen desea visualizar?', genes)
    
    # Filtrar los datos según el gen seleccionado
    df_filtered_by_input_gene = df.loc[(df['Gen'] == gene)]
    df_filtered_relevant = df_filtered_by_input_gene[['Gen', 'Mutated Aminoacid', 'Mutated Codon']].sort_values(['Gen', 'Mutated Aminoacid', 'Mutated Codon'], ascending=[True, True, True])
    
    # Generar DataFrame con la frecuencia de aparición de cada codón
    codon_count = df_filtered_relevant.groupby('Mutated Aminoacid')['Mutated Codon'].value_counts().to_frame(name='Counts').reset_index()
    
    # Generar gráfico
    fig_title = f"Aminoácidos mutados y los codones que codifican para el gen {gene}"
    fig = px.bar(codon_count, x='Mutated Aminoacid', y='Counts', color='Mutated Codon', title=fig_title)
    st.plotly_chart(fig)
