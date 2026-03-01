import os

def clean_terminal():
    '''Отчищает терминал'''
    os.system('cls')

def print_emty_rows(n: int) -> None:
    '''Печатает n пустых строк'''
    print('\n'*n)


    