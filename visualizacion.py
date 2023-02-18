'''
Visualización de resultados Liponium:
Gráfico de barras segmentadas para cada aminoácido mutado del gen elegido
En construcción
@ Andrea Ross
'''

#Librerias
import pandas as pd
import argparse
import plotly.express as px


#Tomar el archivo de entrada e imprimir un mensaje solicitando los genes a analizar (Para empezar solo 1 gen)'''
parser = argparse.ArgumentParser(
                    prog = 'Codon Visualizer',
                    description = 'Generador de gráficos de barras segmentadas para distinguir entre los distintos codones mutados')
parser.add_argument('file', help= 'File to read')
args = parser.parse_args()

df = pd.read_excel(args.file)
gene = input("¿Qué gen desea visualizar? ")

#Realizar un nuevo DataFrame únicamente con el gen que se quiere visualizar y filtrarlo de forma que solo se tenga la info relevante para el gráfico
df_filtered_by_input_gene = df.loc[(df['Gen'] == gene)]
df_filtered_relevant = df_filtered_by_input_gene[['Gen', 'Mutated Aminoacid', 'Mutated Codon']].sort_values(['Gen', 'Mutated Aminoacid', 'Mutated Codon'] , ascending=[True, True, True])

#Generar DataFrame con la frecuencia de aparición de cada codón
codon_count = df_filtered_relevant.groupby('Mutated Aminoacid')['Mutated Codon'].value_counts().to_frame(name='Counts').reset_index()

#Generar gráfico
fig_title = ("Aminoácidos mutados y los codones que codifican para el gen " + gene)
fig = px.bar(codon_count, x='Mutated Aminoacid', y='Counts', color='Mutated Codon', title = fig_title)
fig.show()


