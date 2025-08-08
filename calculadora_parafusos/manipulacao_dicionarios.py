tamanhos_parafusos = [
    150,
    200,
    250,
    300,
    350,
    400,
    450,
    500,
    550,
    600,
    650,
    700,
    750,
    800,
    850,
    900,
    950,
    1000,
]

dicionario_coeficiente = [
    [600, 0],
    [1000, 1.5],
    [1500, 3],
    [2000, 4.5],
    [2500, 6],
    [3000, 7.5],
]

dicionario_conicidade_topo = [["TOPO", 28, 140], ["GAVETA", 20, 110]]

dicionario_comprimento_materiais = {
    "CRUZETA": 105,
    "ARRUELA": 4,
    "PORCA": 11,
    "SOBRA": 11,
    "OLHAL": 16,
}


def coeficiente_conicidade_topo(carga, posicao, dic1, dic2):
    coeficiente_tipo = 0
    conicidade = 0
    valor_inicial_topo = 0

    for valor, coef in dic1:
        if valor == carga:
            coeficiente_tipo = coef

    for valor, coni, topo in dic2:
        if valor == posicao:
            conicidade = coni
            valor_inicial_topo = topo

    return coeficiente_tipo, conicidade, valor_inicial_topo


if __name__ == "__main__":
    a, b, c = coeficiente_conicidade_topo(
        1500, "GAVETA", dicionario_coeficiente, dicionario_conicidade_topo
    )
    print(a, b, c)
