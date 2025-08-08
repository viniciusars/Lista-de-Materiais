import pandas as pd


def valores_tabela_locacao_parafuso():
    tabela_locacao = pd.read_csv("./data/Tabela_de_Locacao.csv", encoding="latin-1")
    elementos_especificos = tabela_locacao[["Tipo", "Posição"]].copy()
    elementos_especificos[["Altura", "Carga"]] = tabela_locacao[
        "Altura/carga"
    ].str.split("/", expand=True)
    elementos_especificos = elementos_especificos[:-1]

    estruturas_tipicas = elementos_especificos[
        ~elementos_especificos["Tipo"].str.contains("CH")
    ]
    estruturas_tipicas = estruturas_tipicas.drop(["Altura"], axis=1)
    estruturas_tipicas = estruturas_tipicas.value_counts().reset_index(
        name="Quantidade"
    )

    estruturas_especiais = elementos_especificos[
        elementos_especificos["Tipo"].str.contains("CH")
    ]
    estruturas_especiais = estruturas_especiais.value_counts().reset_index(
        name="Quantidade"
    )

    return estruturas_tipicas, estruturas_especiais


if __name__ == "__main__":
    tipicas, especiais = valores_tabela_locacao_parafuso()
    print(tipicas)
