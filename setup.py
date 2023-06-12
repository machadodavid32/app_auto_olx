import sys
from cx_Freeze import setup, Executable


# Definindo as dependências

build_exe_options = {'packages': ['os'], 'includes': ['tkinter']}

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'
    
setup(
    name= "olx_dados",
    version= '2.1',
    description='Este programa automatiza coleta de dados dos resultados de uma pesquisa de produtos na olx',
    author='David Machado',
    options={'build_exe':build_exe_options},
    executables=[Executable('app_v2.1.py', base=base)]
)    
