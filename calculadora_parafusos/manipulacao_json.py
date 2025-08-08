# import pandas as pd
import json
from json import load
import pandas as pd


def pegar_json():
    with open("./calculadora_parafusos/estruturas.json", "r", encoding="utf-8") as f:
        estruturas = load(f)
    return estruturas


def quant_niveis(tipo):
    arquivo_estruturas_json = pegar_json()
    niveis = arquivo_estruturas_json["estruturas"][tipo]["NIVEIS"]

    return niveis


def dist_niveis(tipo):
    niveis = quant_niveis(tipo)
    array_dist_niveis = []

    arquivo_estruturas_json = pegar_json()
    estrutura = arquivo_estruturas_json["estruturas"][tipo]

    for c in range(1, niveis + 1):
        if c == 1:
            array_dist_niveis.append(estrutura[f"NIVEL {c}"]["DISTANCIA"])
        else:
            array_dist_niveis.append(
                estrutura[f"NIVEL {c}"]["DISTANCIA"]
                + estrutura[f"NIVEL {c-1}"]["DISTANCIA"]
            )

    return array_dist_niveis


def elementos_niveis(tipo):
    niveis = quant_niveis(tipo)
    arquivo_estruturas_json = pegar_json()
    array_dist_niveis = dist_niveis(tipo)

    array_elementos_niveis = [
        [
            "NIVEL",
            "ALTURA",
            "CRUZETA",
            "PARAFUSO SIMPLES",
            "PARAFUSO DUPLO",
            "ARRUELA",
            "PORCA",
            "PORCA OLHAL",
            "SOBRA",
        ]
    ]

    estrutura = arquivo_estruturas_json["estruturas"][tipo]

    cont = 1
    for c in range(1, niveis + 1):

        nivel = estrutura[f"NIVEL {c}"]["CONSTRUCAO"]

        for x in range(0, len(nivel)):
            array_elementos_niveis.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

            array_elementos_niveis[cont][0] = c
            array_elementos_niveis[cont][1] = array_dist_niveis[c - 1]

            padrao = arquivo_estruturas_json["padroes"][nivel[x]]
            padrao = list(padrao.values())

            for y in range(0, len(padrao)):
                array_elementos_niveis[cont][y + 2] = padrao[y]

            cont += 1

    array_elementos_niveis = pd.DataFrame(
        array_elementos_niveis[1:], columns=array_elementos_niveis[0]
    )

    return array_elementos_niveis


if __name__ == "__main__":
    x = elementos_niveis("N4/N4.N3")
    print(x)
