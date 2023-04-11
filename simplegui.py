import PySimpleGUI as sg
import webbrowser
import pyautogui
from time import sleep
from threading import Thread

sg.theme('LightBrown')



layout = [
    [sg.Text("Digite seu usuario: ")],
    [sg.Input(key='usuario')],
    [sg.Text('Digite sua senha: ')],
    [sg.Input(password_char='*', key='senha')],
    [sg.Text('O que pesquisar?')],
    [sg.Input(key='pesquisa')],
    [sg.Text('Digite seu comentário')],
    [sg.Input(key='comentario')],
    [sg.Button('Start')],
    [sg.Output(size=(60,10))]    
]

window = sg.Window('InstaAuto', layout=layout)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Start':
        thread_inicio = Thread(target='Start', daemon=True)
        thread_inicio.start()
        usuario = values['usuario']
        senha = values['senha']
        pesquisa = values['pesquisa']
        comentario = values['comentario']
        
        sleep(3)
        
        webbrowser.open_new_tab('https://www.instagram.com')
        sleep(2)
        
        # Trocar de conta
        pyautogui.click(1224,648, duration=2)
        
        # login
        pyautogui.click(1047,379, duration=2)
        pyautogui.typewrite(usuario)
        sleep(2)
        
       
        # Senha
        pyautogui.click(1135,419, duration=2)
        pyautogui.typewrite(senha)
        sleep(2)
    
        
        # Entrar
        pyautogui.click(1129,464, duration=1)
        sleep(2)
        
        casa = pyautogui.locateCenterOnScreen('casa.png')
        casa_escura = pyautogui.locateCenterOnScreen('casa_escura.png')
        if casa or casa_escura is None:
            print('Usuário ou senha incorretos.')
        
        else:    
            print('Automação Iniciada')
            # Não salvar
            pyautogui.click(1044,613, duration=1)
        
            # 2 - clicar em pesquisar
            pyautogui.click(54,282,duration=1.5)
            sleep(1)
            # Escrevendo o que pesquisar
            pyautogui.typewrite(pesquisa)
            
            # Clicando no resultado da pesquisa
            pyautogui.click(243,311, duration=1)
            sleep(1)
            
            
            # Mover até a publicação
            pyautogui.moveTo(682,761,duration=2)
            sleep(5)
            # Clicar na publicação
            pyautogui.click(683,768,duration=1)
            sleep(3)
            # Clicar em curtir
            pyautogui.click(1115,869,duration=1)
            sleep(2)
            pyautogui.click(947,881, duration=2)
            sleep(2)
            
        
            # 10 - Verificar se já curti ou não aquela postagem
            coracao = pyautogui.locateCenterOnScreen('coracao.png')
            sleep(1)
            # 11 - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas
            if coracao is not None:
                sleep(86400)
            # 12 - Se não tiver curtido, curtir a foto
            elif coracao == None:
                pyautogui.click(1140,866,duration=1)
                sleep(5)
                
                # 13 - Se não tiver curtido, comentar na foto
                pyautogui.click(1205,980,duration=2)
                sleep(3)
                
                # 14 - Escrevendo o comentário
                pyautogui.typewrite(comentario)
                sleep(2)
                
                # 15 - Clicando em publicar
                pyautogui.click(1571,979, duration=2)
                sleep(2)   
                
                # Repetindo passos do 13 ao 15 em outra posição
                
                # comentar
                pyautogui.click(1174,981, duration=2)
                sleep(2)
                # Escrever
                pyautogui.typewrite(comentario)
                sleep(2)
                # clicando em publicar
                pyautogui.click(1378,985, duration=2)
                sleep(3)
                
                # Para sair do site
                pyautogui.click(33,984, duration=1)
                sleep(2)
                pyautogui.click(33,984, duration=1)
                sleep(2)
                # Deslogar
                pyautogui.click(46,922, duration=2)
                sleep(1)
                break
            
    