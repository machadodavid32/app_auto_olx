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
        thread_inicio = Thread(target='Start', args=(window,values, 'Start'), daemon=True)
        thread_inicio.start()
        pesquisa = values['pesquisa']
        query = values[0]
        
    sleep(3)


    try:    
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
        driver.implicitly_wait(10)
        
        # Entrar na página - ok 17/09/2024
        driver.get('https://www.olx.com.br/brasil')
        
        # Botão busca - ok 17/09/2024
        busca = driver.find_element(By.XPATH,"//input[contains(@class, 'olx-text-input__input-field') and contains(@class, 'olx-text-input__input-field--medium')]") 
        busca.click()
        busca.send_keys(pesquisa) # enviando
             
        
        # Clicando em buscar 17/09/2024
        botao_busca = driver.find_element(By.CLASS_NAME, '_2dsuYh')
        botao_busca.click()
        
        # Escolhendo o estado
        #br = driver.find_element(By.XPATH,"//li[@class='olx-dropdown__native olx-dropdown__native--medium olx-dropdown__native--icon-left olx-dropdown__native--icon-left--medium']")
        #br.click()
        
        
        if query == 'Acre':
            ac = driver.find_element(By.LINK_TEXT,'Acre')
            ac.click()
            
            
        if query == 'Alagoas':
            al = driver.find_element(By.LINK_TEXT,'Alagoas')
            al.click()
                
        
        if query == 'Amapá':
            ap = driver.find_element(By.LINK_TEXT, 'Amapá')
            ap.click()
            
                    
        if query == 'Amazonas':
            am = driver.find_element(By.LINK_TEXT, 'Amazonas')
            am.click()
            
                
        if query == 'Bahia':
            ba = driver.find_element(By.LINK_TEXT, 'Bahia')
            ba.click()
            
            
        if query == 'Ceará':
            ce = driver.find_element(By.LINK_TEXT, 'Ceará')
            ce.click()
            
            
        if query == 'Distrito Federal':
            df = driver.find_element(By.LINK_TEXT, 'Distrito Federal')
            df.click()
            
            
        if query == 'Espírito Santo':
            es = driver.find_element(By.LINK_TEXT, 'Espírito Santo')
            es.click()
            
            
        if query == 'Goiás':
            go = driver.find_element(By.LINK_TEXT, 'Goiás')
            go.click()
                  
            
        if query == 'Maranhão':
            ma = driver.find_element(By.LINK_TEXT, 'Maranhão')
            ma.click()
                    
            
        if query == 'Mato Grosso':
            mt = driver.find_element(By.LINK_TEXT, 'Mato Grosso')
            mt.click()
              
            
        if query == 'Mato Grosso do Sul':
            ms = driver.find_element(By.LINK_TEXT, 'Mato Grosso do Sul')
            ms.click()
                     
            
        if query == 'Minas Gerais':
            mg = driver.find_element(By.LINK_TEXT, 'Minas Gerais')
            mg.click()
            
            
        if query == 'Pará':
            pa = driver.find_element(By.LINK_TEXT, 'Pará')
            pa.click()
            
            
        if query == 'Paraíba':
            pb = driver.find_element(By.LINK_TEXT, 'Paraíba')
            pb.click()
            
            
        if query == 'Paraná':
            pr = driver.find_element(By.LINK_TEXT, 'Paraná')
            pr.click()
            
            
        if query == 'Pernanbuco':
            pe = driver.find_element(By.LINK_TEXT, 'Pernanbuco')
            pe.click()
            
            
        if query == 'Piauí':
            pi = driver.find_element(By.LINK_TEXT, 'Piauí')
            pi.click()
            
            
        if query == 'Rio de Janeiro':
            rj = driver.find_element(By.LINK_TEXT, 'Rio de Janeiro')
            rj.click()
            
            
        if query == 'Rio Grande do Norte':
            rn = driver.find_element(By.LINK_TEXT, 'Rio Grande do Norte')
            rn.click()
            
            
        if query == 'Rio Grande do Sul':
            rs = driver.find_element(By.LINK_TEXT, 'Rio Grande do Sul')
            rs.click()
            
            
        if query == 'Rondônia':
            ro = driver.find_element(By.LINK_TEXT, 'Rondônia')
            ro.click()
            
            
        if query == 'Roraima':
            rr = driver.find_element(By.LINK_TEXT, 'Roraima')
            rr.click()
            
            
        if query == 'Santa Catarina':
            sc = driver.find_element(By.LINK_TEXT, 'Santa Catarina')
            sc.click()
            
            
        if query == 'São Paulo':
            sp = driver.find_element(By.LINK_TEXT, 'São Paulo')
            sp.click()
            
            
        if query == 'Sergipe':
            se = driver.find_element(By.LINK_TEXT, 'Sergipe')
            se.click()
            
            
        if query == 'Tocantins':
            to = driver.find_element(By.LINK_TEXT, 'Tocantins')
            to.click()
                     
        
    except:
        print("Problemas de conexão. Está conectado á internet?")
    
    #while True:
     #   driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight / 2);')
        


                        # Class anuncio normal: kgl1mq-0 eFXRHn sc-ifAKCX iUMNkO
                        # Class anuncio destaque: kgl1mq-0 eFXRHn sc-ifAKCX ghBVzA   
                        # São classes diferentes, preciso achar algo incomum
                        # Achei esta: //div[@class='sc-12rk7z2-7 kDVQFY'] 
                        # Como queremos os titulos pra jogar na tabela, é só ir na tag mãe h2 desta forma; //div[@class='sc-12rk7z2-7 kDVQFY']//h2

        titulos = driver.find_elements(By.XPATH,"//div[@class='sc-12rk7z2-7 kDVQFY']//h2")

        # Agora devemos pesquisar os preços:
        precos = driver.find_elements(By.XPATH, "//div[@class='sc-1kn4z61-1 dGMPPn']")
        links = driver.find_elements(By.XPATH, "//a[@data-lurker-detail='list_id']")

        # Guardar esses dados em arquivos CSV
        for titulo, preco, link in zip(titulos, precos, links):
            with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
                    link_processado = link.get_attribute('href')   # href é o atributo onde se encontra de fato o link
                    arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')  #os.linesep é uma quebra de linha para organizar as linhas
        try:               
            proxima_pagina = driver.find_element(By.XPATH, "//span[text()='Próxima página']")    
            
            proxima_pagina.click()
            
        except:
            print('Fim da extração')
            break      
        


input('')
driver.close()    