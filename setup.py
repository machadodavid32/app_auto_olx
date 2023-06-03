import sys
from cx_Freeze import setup, Executable

# Definindo as dependências

build_exe_options = {'packages': ['os'], 'includes': ['tkinter']}

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'
    
setup(
    name= "olx_dados",
    version= '1.0',
    description='Este programa tem como objetivo curtir e adicionar comentários em diversas páginas no Instagram',
    options={'build_exe':build_exe_options},
    executables=[Executable('app_v02.py', base=base)]
)    
