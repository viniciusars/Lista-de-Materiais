import pandas as pd

tabela_locacao = pd.read_csv('./data/Tabela_de_Locacao.csv', encoding='latin-1')
elementos_especificos = tabela_locacao[['Tipo', 'Posição']].copy()
elementos_especificos[['Altura', 'Carga']] = tabela_locacao['Altura/carga'].str.split('/', expand=True)
elementos_especificos = elementos_especificos[:-1]

estruturas_tipicas = elementos_especificos[~elementos_especificos['Tipo'].str.contains('CH')]
estruturas_tipicas = estruturas_tipicas.drop(['Carga'],axis=1)
estruturas_tipicas = estruturas_tipicas.value_counts().reset_index(name='Quantidade')

estruturas_especiais = elementos_especificos[elementos_especificos['Tipo'].str.contains('CH')]
estruturas_especiais = estruturas_especiais.value_counts().reset_index(name='Quantidade')

print(estruturas_especiais)

