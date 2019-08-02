import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import time
import pandas as pd
import pickle
import os


PLOSONE = 'https://journals.plos.org/plosone/browse?resultView=list&page='

ano2019 = range(1, 772)
total = range(1, 17034)

driver = webdriver.Firefox()
driver.get(PLOSONE + '1')

articlesEditorName = []
articlesSubject = []
articleID = []
id = 0
articesurl = []
articlesDate = []
ano = 2019
for i in ano2019:
    driver.get(PLOSONE + str(i))
    # time.sleep(0.5)
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#subject-list-view > #search-results > li > h2 > a.list-title")))
    # elements = driver.find_elements_by_css_selector("#subject-list-view > #search-results > li > h2 > a.list-title")
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

        # if date != '-':
        #     if int(date) < ano:
        #         df = pd.DataFrame()
        #         df['nome'] = articlesEditorName
        #         df['area'] = articlesSubject
        #         df['url'] = articesurl
        #         df['data'] = articlesDate
        #         df.to_csv('dev/articles_' + str(ano) + '.csv', sep = ';', encoding = 'utf-8', index = False)
        #         ano -= 1
        subjectAreas = driver.find_element_by_id('subjectList').find_elements_by_tag_name('a')
        id += 1

        for subject in subjectAreas:
            articlesSubject.append(subject.text)
            articleID.append(id)
            articlesDate.append(date)
            articlesEditorName.append(editorName)
            articesurl.append(url)
df = pd.DataFrame()
df['identificador'] = articleID
df['area'] = articlesSubject
df['nome'] = articlesEditorName
df['url'] = articesurl
df['data'] = articlesDate
df.to_csv('dev/articles.csv', sep=';', encoding='utf-8', index=False)