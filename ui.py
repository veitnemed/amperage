import os
import time 
from datetime import date
import analytics as anl
import storage

TITTLE = 'MEAN AMPERAGE V.1.0'

SHOW_COLUMNS = '               |                   Ток джаммера, A                   |         |          |'
SHOW_COLUMNS_2 = ' Номер ССБ 115 |                                                     |   Σ,A   |   Дата   |'
SECOND_COLUMNS = '               |  0.8   |  1.4   |  4.9   |  5.3   |  5.5   |  5.9   |         |          |'
SEPORATOR = '==========================================================================================|'

DATE_FORMAT = '%d %b'
def clean_terminal():
    '''Отчищает терминал'''
    os.system('cls')


def print_emty_rows(n: int) -> None:
    '''Печатает n пустых строк'''
    print('\n'*n)

def emptsep(n: int) -> str:
    return ' '*n + '|'

def empts(n: int) -> str:
    return ' '*n

def print_seporator():
        '''Печататет:
        ===============================
        '''
        print('='*72)


# === START ==== 
def show_main_menu():
    print('\n', SEPORATOR, '\n')
    print('1. Показать статистику')
    print('2. Добавить данные об ССБ 115')
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

def show_all_rows(rows: list) -> None:
    '''Показывает все записи с красивым выводом'''
    
    print(SEPORATOR)
    print(SHOW_COLUMNS)
    print(SECOND_COLUMNS)
    print(SEPORATOR)
    for row in rows:
        tottal_amp = 0
        serial, *amps, dt_iso = row
        
        date_obj = date.fromisoformat(dt_iso)
        date_format = date_obj.strftime(DATE_FORMAT)
        
        print('№ '+serial, end='      ')
        for amp in amps:
            n = str(round(float(amp),1))
            print(amp.rjust(4), end='     ')
            tottal_amp += float(amp)
        print(' ',str(round(tottal_amp,1)).rjust(4), end ='   ')
        print(date_format.rjust(7))

def show_all_rows(rows: list) -> None:
    '''Показывает все записи с красивым выводом'''
    
    print(SEPORATOR)
    print(SHOW_COLUMNS)
    print(SHOW_COLUMNS_2)
    print(SECOND_COLUMNS)
    print(SEPORATOR)
    for row in rows:
        tottal_amp = 0
        serial, *amps,tottal, dt = row
        
        print(empts(2)+serial + emptsep(2),end = '')
        for amp in amps:
            print(empts(1)+amp+emptsep(3),end='')
        print(empts(2)+tottal+emptsep(3), end='')
        print(empts(1)+dt+emptsep(2))
    print(SEPORATOR)
   
        

        


