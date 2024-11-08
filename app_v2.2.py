'''
Projeto monitoramento de preços OLX
Passos:
1 - Entrar na pagina.
2 - Localizar campo de busca
3 - clicar em campo de busca
4 - digitar o alvo

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import os
import PySimpleGUI as sg
from threading import Thread

from features.navigation import navegar_para_estado # Importando a função criada


layout = [
    [sg.Text("O que deseja pesquisar?")],
    [sg.Input(key='pesquisa')],
    [sg.Text('Selecione o local')],
    [sg.Combo(values=['Brasil', 'Acre', 'Alagoas', 'Amapá', 'Amazonas',
                      'Bahia', 'Ceará', 'Distrito Federal',
                      'Espírito Santo', 'Goiás', 'Maranhão',
                      'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais',
                      'Pará', 'Paraíba', 'Paraná', 'Pernanbuco',
                      'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte',
                      'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina',
                      'São Paulo', 'Sergipe', 'Tocantins'], default_value='Brasil')],
    [sg.Button('Start')],
    [sg.Output(size=(60,10))]    
]

window = sg.Window('Auto_olx', layout=layout)

def iniciar_driver():
    chrome_options = Options()
    #arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--incognito']
    arguments = ['--lang=pt-BR', '--start-maximized', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def iniciar_busca(window, values):
    pesquisa = values['pesquisa']
    query = values[0]
    driver = iniciar_driver()
    driver.implicitly_wait(10)
    
    # Entrar na página - ok 17/09/2024
    driver.get('https://www.olx.com.br')
    
    # Navegar para o estado selecionado
    navegar_para_estado(driver, query)
    
    busca = driver.find_element(By.XPATH, "//input[contains(@class, 'olx-text-input__input-field') and contains(@class, 'olx-text-input__input-field--medium')]") 
    busca.click()
    busca.send_keys(pesquisa) # enviando
    
    while True:
        next_page = driver.find_element(By.XPATH, "//span[text()='Próxima página']")
        driver.execute_script("arguments[0].scrollIntoView();", next_page)
        next_page.click()
    
        titulos = driver.find_elements(By.XPATH, "//div[@class='sc-12rk7z2-7 kDVQFY']//h2")
        precos = driver.find_elements(By.XPATH, "//div[@class='sc-1kn4z61-1 dGMPPn']")
        links = driver.find_elements(By.XPATH, "//a[@data-lurker-detail='list_id']")

        # Guardar esses dados em arquivos CSV
        for titulo, preco, link in zip(titulos, precos, links):
            with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
                link_processado = link.get_attribute('href')
                arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')
        
        try:
            proxima_pagina = driver.find_element(By.XPATH, "//span[text()='Próxima página']")
            proxima_pagina.click()
        except:
            print('Fim da extração')
            break

    driver.close()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Start':
        thread_inicio = Thread(target=iniciar_busca, args=(window, values), daemon=True)
        thread_inicio.start()

input('')
