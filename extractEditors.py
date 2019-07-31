from selenium import webdriver
from selenium.common import exceptions
import time
import pandas as pd
import pickle
import os


PLOSONE = 'https://journals.plos.org/plosone/static/editorial-board'


driver = webdriver.Firefox()
driver.get(PLOSONE)


nomesEditores = []
orcidEditor = []
instituicaoEditores = []
paisEditores = []
areaEditores = []

while True:
    editores = driver.find_element_by_css_selector('.editors-list')
    list_elements_editors = editores.find_elements_by_class_name('item')
    for editor in list_elements_editors:
        texto = editor.text
        editorDados = texto.split('\n')
        if 'orcid' in editorDados[1]:
            nomesEditores.append(editorDados[0])
            orcidEditor.append(editorDados[1])
            instituicaoEditores.append(editorDados[2])
            paisEditores.append(editorDados[3])
            areaEditores.append(editorDados[4][14:].split(', '))
        else:
            nomesEditores.append(editorDados[0])
            orcidEditor.append('-')
            instituicaoEditores.append(editorDados[1])
            paisEditores.append(editorDados[2])
            areaEditores.append(editorDados[3][15:].split(', '))
    if len(list_elements_editors) < 50:
        break
    nextButton = driver.find_element_by_css_selector('nav.nav-pagination:nth-child(2) > a:nth-child(9)')
    nextButton.click()
    time.sleep(1)
df = pd.DataFrame()
areasList = []
nomesList = []
for i, area in enumerate(areaEditores):
    for x in area:
        areasList.append(x)
        nomesList.append(nomesEditores[i])
df['area'] = areasList
df['nome'] = nomesList
df.to_csv('dev/plosEditoresAreas.csv',sep=';',encoding='utf-8',index=False)
df = pd.DataFrame()
df['nome'] = nomesEditores
df['instituicao'] = instituicaoEditores
df['pais'] = paisEditores
df['orcid'] = orcidEditor
df.to_csv('dev/plosEditoresComplementar.csv', sep=';', encoding='utf-8', index=False)
