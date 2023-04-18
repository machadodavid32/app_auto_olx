import PySimpleGUI as sg

sg.theme('Reddit')

layout_login = [
    [sg.Text('Usuário')],
    [sg.Input(size=(32, 1))],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', size=(32, 1))],
    [sg.Button('Salvar usuário e senha')],
    [sg.Text(key='dados_usuario')]
]

layout_velocidade = [
    [sg.Text('Velocidade da automação')],
    [sg.Radio('Lento', group_id='velocidade'), sg.Radio(
        'Normal', group_id='velocidade'), sg.Radio('Rápido', group_id='velocidade')],
    [sg.Text('Requisições por minuto')],
    [sg.Slider(range=(1, 500), orientation='h')],
    [sg.Combo(values=['Iniciante', 'Intermediário', 'Avançado'],
              default_value='Iniciante')],
    [sg.Button('Salvar configurações')]
]

layout_sites = [
    [sg.Text('Quais sites devem ser automatizados?')],
    [sg.Checkbox('Site 1'), sg.Checkbox('Site 2'), sg.Checkbox('Site 3')],
    [sg.Button('Salvar configurações sites')]
]

layout_atividades = [
    [sg.Text('Atividades')],
    [sg.Output(size=(66, 7))]
]

layout_principal = [
    [sg.Frame('Login', layout_login), sg.TabGroup([
        [sg.Tab('Velocidade', layout_velocidade)],
        [sg.Tab('Sites', layout_sites)]
    ])],
    [sg.Frame('Log de atividades', layout_atividades)],
    [sg.Button('Iniciar automações')]
]

window = sg.Window('Automação de sites', layout=layout_principal)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar usuário e senha':
        window['dados_usuario'].update('Dados salvos com sucesso')
        print('Usuário e senha cadastrados')
    elif event == 'Salvar configurações':
        print('Configurações de velocidade salvas com sucesso!')
    elif event == 'Salvar configurações sites':
        print('Salvo configurações de sites')
    elif event == 'Iniciar automações':
        print('Iniciando automações')