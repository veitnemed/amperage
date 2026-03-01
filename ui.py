import os
import time 

TITTLE = 'MEAN AMPERAGE V.1.0'
start = 'start'
end = 'end'

def clean_terminal():
    '''Отчищает терминал'''
    os.system('cls')


def print_emty_rows(n: int) -> None:
    '''Печатает n пустых строк'''
    print('\n'*n)

def print_seporator():
        '''Печататет:
        
        ===============================
        
        '''
        print_emty_rows(0)
        print('='*72)
        print_emty_rows(0)

# === START ==== 

def show_tittle():
    '''Выводим название программы'''
    print_seporator()
    print(' '*24,TITTLE) 
    print_seporator()

def show_post_tittlee():

    print('Утилита предназначена для учета серийных номеров')
    print('И учета статистических значений тока')

def complete_write(s,fact):
    print(f'\n Значения панели № {s} ({fact}) записаны!\n')
    time.sleep(3)
    
    

    