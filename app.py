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


    driver = iniciar_driver()
    # Entrar na página
    driver.get('https://www.olx.com.br/')
    sleep(5)
    
    driver.execute_script("window.scrollTo(0, 900);")
    sleep(5)
        
    if query == 'Brasil':
        br = driver.find_element(By.LINK_TEXT,'BRASIL')
        br.click()
        sleep(5)
    
    elif query == 'Acre':
        ac = driver.find_element(By.XPATH, "//a[text()='ac']")
        ac.click()
        sleep(5)
        
    elif query == 'Alagoas':
        al = driver.find_element(By.XPATH, "//a[text()='al']")
        al.click()
        sleep(5)   
    
    elif query == 'Amapá':
        ap = driver.find_element(By.XPATH, "//a[text()='ap']")
        ap.click()
        sleep(5)
                
    elif query == 'Amazonas':
        am = driver.find_element(By.XPATH, "//a[text()='am']")
        am.click()
        sleep(5)
            
    elif query == 'Bahia':
        ba = driver.find_element(By.XPATH, "//a[text()='ba']")
        ba.click()
        sleep(5)
        
    elif query == 'Ceará':
        ce = driver.find_element(By.XPATH, "//a[text()='ce']")
        ce.click()
        sleep(5)
        
    elif query == 'Distrito Federal':
        df = driver.find_element(By.XPATH, "//a[text()='df']")
        df.click()
        sleep(5)
        
    elif query == 'Espírito Santo':
        es = driver.find_element(By.XPATH, "//a[text()='es']")
        es.click()
        sleep(5)
        
    elif query == 'Goiás':
        go = driver.find_element(By.XPATH, "//a[text()='go']")
        go.click()
        sleep(5)       
        
    elif query == 'Maranhão':
        ma = driver.find_element(By.XPATH, "//a[text()='ma']")
        ma.click()
        sleep(5)        
        
    elif query == 'Mato Grosso':
        mt = driver.find_element(By.XPATH, "//a[text()='mt']")
        mt.click()
        sleep(5)    
        
    elif query == 'Mato Grosso do Sul':
        ms = driver.find_element(By.XPATH, "//a[text()='ms']")
        ms.click()
        sleep(5)            
        
    elif query == 'Minas Gerais':
        mg = driver.find_element(By.XPATH, "//a[text()='mg']")
        mg.click()
        sleep(5)
        
    elif query == 'Pará':
        pa = driver.find_element(By.XPATH, "//a[text()='pa']")
        pa.click()
        sleep(5)
        
    elif query == 'Paraíba':
        pb = driver.find_element(By.XPATH, "//a[text()='pb']")
        pb.click()
        sleep(5)
        
    elif query == 'Paraná':
        pr = driver.find_element(By.XPATH, "//a[text()='pr']")
        pr.click()
        sleep(5)
        
    elif query == 'Pernanbuco':
        pe = driver.find_element(By.XPATH, "//a[text()='pe']")
        pe.click()
        sleep(5)
        
    elif query == 'Piauí':
        pi = driver.find_element(By.XPATH, "//a[text()='pi']")
        pi.click()
        sleep(5)
        
    elif query == 'Rio de Janeiro':
        rj = driver.find_element(By.XPATH, "//a[text()='rj']")
        rj.click()
        sleep(5)
        
    elif query == 'Rio Grande do Norte':
        rn = driver.find_element(By.XPATH, "//a[text()='rn']")
        rn.click()
        sleep(5)
        
    elif query == 'Rio Grande do Sul':
        rs = driver.find_element(By.XPATH, "//a[text()='rs']")
        rs.click()
        sleep(5)
        
    elif query == 'Rondônia':
        ro = driver.find_element(By.XPATH, "//a[text()='ro']")
        ro.click()
        sleep(5)
        
    elif query == 'Roraima':
        rr = driver.find_element(By.XPATH, "//a[text()='rr']")
        rr.click()
        sleep(5)
        
    elif query == 'Santa Catarina':
        sc = driver.find_element(By.XPATH, "//a[text()='sc']")
        sc.click()
        sleep(5)
        
    elif query == 'São Paulo':
        sp = driver.find_element(By.XPATH, "//a[text()='sp']")
        sp.click()
        sleep(5)
        
    elif query == 'Sergipe':
        se = driver.find_element(By.XPATH, "//a[text()='se']")
        se.click()
        sleep(5)
        
    elif query == 'Tocantins':
        to = driver.find_element(By.XPATH, "//a[text()='to']")
        to.click()
        sleep(5)          



     
  
    # Localizar campo de busca
    campo_busca = driver.find_elements(By.XPATH, "//div[@class='h3us20-4 cxGeqJ']//header[@id='header']")
    sleep(3)
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

    while True:
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
            