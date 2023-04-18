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
from time import sleep
import os
import PySimpleGUI as sg
from threading import Thread
import random


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



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Start':
        thread_inicio = Thread(target='Start', daemon=True)
        thread_inicio.start()
        pesquisa = values['pesquisa']
        query = values[0]
    
    sleep(3)



    def iniciar_driver():
        chrome_options = Options()
        arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--incognito']
        for argument in arguments:
            chrome_options.add_argument(argument)

        chrome_options.add_experimental_option('prefs', {
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.automatic_downloads': 1,

        })
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=chrome_options)

        return driver

    def digitar_naturalmente(texto, elemento):
        for letra in texto:
            elemento.send_keys(pesquisa)
            sleep(random.randint(1, 5)/30)


    driver = iniciar_driver()
    # Entrar na página
    driver.get('https://www.olx.com.br/')
    sleep(5)
    
    driver.execute_script("window.scrollTo(0, 800);")
    sleep(5)
    
    if query == 'Acre':
        ac = driver.find_element(By.LINK_TEXT,'AC')
        ac.click()
        sleep(3)
        
        

    # Localizar campo de busca
    campo_busca = driver.find_element(By.ID,"searchtext-input")
    # Clicando no campo de busca
    campo_busca.click()
    sleep(2)
    
    #Digitando no campo de pesquisa
    campo_busca.send_keys(pesquisa)
    sleep(2)

    # Achar campo busca em buscar
    botao_busca = driver.find_element(By.CLASS_NAME, 'search-button-submit')
    sleep(2)
    # Clicando no botão de busca
    botao_busca.click()
    sleep(8)

    # Xpath dos EStados:

    br = driver.find_element(By.XPATH, "//a[text()='Brasil']") 
    br.click()
    sleep(5)
    
    
    #if 'Acre':
     #   ac = driver.find_element(By.XPATH, "//a[text()='Acre']") 
      #  ac.click()
       # sleep(5)
     
    #elif 'Alagoas':
     #   al = driver.find_element(By.XPATH, "//a[text()='Alagoas']") 
      #  al.click()
       # sleep(5)   
    

    while True:
    # Não esquecer de mover até o final da pagina.
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(2)


            # Class anuncio normal: kgl1mq-0 eFXRHn sc-ifAKCX iUMNkO
            # Class anuncio destaque: kgl1mq-0 eFXRHn sc-ifAKCX ghBVzA   
            # São classes diferentes, preciso achar algo incomum
            # Achei esta: //div[@class='sc-12rk7z2-7 kDVQFY'] 
            # Como queremos os titulos pra jogar na tabela, é só ir na tag mãe h2 desta forma; //div[@class='sc-12rk7z2-7 kDVQFY']//h2

        titulos = driver.find_elements(By.XPATH,"//div[@class='sc-12rk7z2-7 kDVQFY']//h2")

            # Agora devemos pesquisar os preços:

        precos = driver.find_elements(By.XPATH, "//div[@class='sc-1kn4z61-1 dGMPPn']")
        links = driver.find_elements(By.XPATH, "//a[@data-lurker-detail='list_id']")

            # estados_todos = driver.find_elements(By.XPATH, '//a[@class="sc-1l6qrj6-0 hSmLZl sc-gzVnrw kGFTcZ"]') 


            # Guardar esses dados em arquivos CSV
        for titulo, preco, link in zip(titulos, precos, links):
             with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
                link_processado = link.get_attribute('href')   # href é o atributo onde se encontra de fato o link
                arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')  #os.linesep é uma quebra de linha para organizar as linhas
        try:        
            proxima_pagina = driver.find_element(By.XPATH, "//span[text()='Próxima pagina']")     
            proxima_pagina.click()
        except:
            print('Fim da extração')
            break      

    input('')
    driver.close()