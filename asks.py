import valid
from datetime import date
import ui
import pyperclip
import time

FREQS = ('0.8','1,4','4,9','5.3','5.5','5.9')
PREFIX = '1525'

lust_nums = {
    '1': 'ВЕКТОР',
    '2': 'ИНТЕГРАЛ',
    '3': 'РЗП',
    '4': 'КНИИТМУ',
    '5': 'СВТ',
    '6': 'СИГНАЛ'
}

def ask_serial_number() -> str:
    ui.print_seporator()
    print('* Серийный номер вида XXXXZ\n')
    print('* Где XXXX - последние 4 цифры')
    print('* Z - номер завода')
    print('* Код можно писать без ведущих нулей\n')
    while True:
        print('Введите серийный код')
        ser = input('>> ')
        if valid.is_correct_serial(ser):
            
            
            return ser
        continue

def ask_value() -> str:
    ui.print_seporator()
    print('Введите потребляемый ток джмара:')
    print('Значение должно быть от 0 до 6 мА (нап. 2.5)\n')
    vals = []
    for freq in FREQS:
        
        while True:
            val = input(f'Введите ток джаммера {freq} >> ')
            if valid.is_cooret_value(val):
                vals.append(float(val))
                break
            print('Ошибка: введите значение от 0 до 6')
            continue
    return tuple(vals)

def code_to_full_serial(code: str) -> str:
    factory = code[-1]
    number = code[:-1]
    return PREFIX + factory + number.rjust(4,'0')

def get_factories_in_full(c):
    z = c[-5]
    if z in lust_nums:
        return lust_nums[z]
    else:
        print(f'Error: factories out of range / {z}')

def get_csv_row():
    code = ask_serial_number()
    serial_number = code_to_full_serial(code)
    pyperclip.copy(serial_number)
    print(f'№ {serial_number} СКОПИРОВАН!')
    time.sleep(2)
    ui.clean_terminal()
    print(f'                       Значения токов для панели № {serial_number}')
    values = ask_value()
    dt_iso = date.today().isoformat()
    return [serial_number,*values,dt_iso]

def is_next_step():
    print()
    while True:
        ans = input('Продолжить? (да/нет) >> ')
        if ans.lower() == 'да':
            return True
        elif ans.lower() == 'нет':
            return False
        else:
            print('Некорректный ввод')
            continue
    
    



