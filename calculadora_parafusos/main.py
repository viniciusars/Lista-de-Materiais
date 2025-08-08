from manipulacao_dicionarios import (
    dicionario_coeficiente,
    dicionario_conicidade_topo,
    dicionario_comprimento_materiais,
    coeficiente_conicidade_topo,
)
from tabela_locacao_parafusos import valores_tabela_locacao_parafuso
from manipulacao_json import elementos_niveis
import pandas as pd


def valor_x(array_valores):
    coeficiente, conicidade, valor_topo = coeficiente_conicidade_topo(
        array_valores["Carga"],
        array_valores["Posição"],
        dicionario_coeficiente,
        dicionario_conicidade_topo,
    )
    x = conicidade * coeficiente + valor_topo
    return x, conicidade


def parafuso_estruturas_tipicas():
    tipicas, especiais = valores_tabela_locacao_parafuso()

    parafusos_calculados = pd.DataFrame(columns=["Tipo", "Parafusos", "Quantidade"])
    tipo = []
    parafuso = []
    quantidade = []

    for index, row in tipicas.iterrows():
        x, conicidade = valor_x(row)

        niveis = elementos_niveis(row["Tipo"])

        for indice, nivel in niveis.iterrows():
            tamanho_parafuso = (
                (
                    (x + conicidade * nivel.iloc[1])
                    + nivel.iloc[2] * dicionario_comprimento_materiais["CRUZETA"]
                )
                + (nivel.iloc[6] * dicionario_comprimento_materiais["PORCA"])
                + (nivel.iloc[5] * dicionario_comprimento_materiais["ARRUELA"])
                + (nivel.iloc[7] * dicionario_comprimento_materiais["OLHAL"])
                + (nivel.iloc[8] * dicionario_comprimento_materiais["SOBRA"])
            )

            parafuso.append(tamanho_parafuso)
            tipo.append(row["Tipo"])
            quantidade.append(row["Quantidade"])

    return parafusos_calculados, tipo, quantidade


if __name__ == "__main__":
    y, x, z = parafuso_estruturas_tipicas()
    print(z)
