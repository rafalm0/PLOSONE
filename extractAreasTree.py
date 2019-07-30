import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import util


df = pd.read_csv('dev/plosAreas.csv', sep=';', encoding='utf-8')
indiceTier = 0
indiceNames = []
AreaDict = {}

for i, line in df.iterrows():
    indiceAtual, nomeIndice = util.tier(line)

    if indiceAtual <= indiceTier:
        x, y = util.acess2(AreaDict, indiceNames)
        x[y] = 0
        for loop in range(0, indiceTier + 1 - indiceAtual):
            indiceNames.pop()

    util.acess(AreaDict, indiceNames)[nomeIndice] = {}
    indiceNames.append(nomeIndice)
    indiceTier = indiceAtual

value_list = util.get_leafs(AreaDict, [])
value_dict = {}
keys = []
for path in value_list:
    key = path[-1]
    value = path[:-1]
    if key not in value_dict:
        value_dict[key] = [value]
    else:
        value_dict[key].append(value)



pass
