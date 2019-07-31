import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from selenium.common import exceptions
import time
import pandas as pd
import pickle
import os


PLOSONE = 'https://journals.plos.org/plosone/browse?resultView=list&page='


driver = webdriver.Firefox()
driver.get(PLOSONE + '1')

articlesEditorName = []
articesurl = []
articlesDate = []
ano = 2019
for i in range(1, 17034):
    driver.get(PLOSONE + str(i))
    time.sleep(0.5)
    elements = driver.find_elements_by_css_selector("#subject-list-view > #search-results > li > h2 > a.list-title")
    linkList = []
    for element in elements:
        linkList.append(element.get_attribute('href'))
    for link in linkList:
        driver.get(link)
        articleInfo = driver.find_element_by_class_name('articleinfo').find_elements_by_tag_name('p')
        date = '-'
        editorName = '-'
        url = '-'
        for tab in articleInfo:
            if 'Editor:' in tab.text:
                editorName = tab.text.split('Editor: ')[1].split(',')[0]
                url = link
            if 'Published:' in tab.text:
                date = tab.text.split('Published: ')[1].split(';')[0].split(',')[1]
        if editorName == '-':
            continue
        if date < ano:
            df = pd.DataFrame()
            df['nome'] = articlesEditorName
            df['url'] = articesurl
            df['data'] = articlesDate
            df.to_csv('dev/articles_' + str(ano) + '.csv', sep = ';', encoding = 'utf-8', index = False)
            ano -= 1
        articlesDate.append(date)
        articlesEditorName.append(editorName)
        articesurl.append(url)
df = pd.DataFrame()
df['nome'] = articlesEditorName
df['url'] = articesurl
df['data'] = articlesDate
df.to_csv('dev/articles.csv', sep=';', encoding='utf-8', index=False)