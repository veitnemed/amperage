from datetime import datetime

lust_nums = {
    '1': 'ВЕКТОР',
    '2': 'ИНТЕГРАЛ',
    '3': 'РЗП',
    '4': 'КНИИТМУ',
    '5': 'СВТ',
    '6': 'СИГНАЛ'
}
# корректный серийник
# корректный ток
# обработка ввода

def is_correct_serial(s: str) -> bool:
    '''Проверка серийного номера
    1. Должен содержать только цифры 
    2. Длина должна быть от 2 до 5 
    3. Последняя цифра  должна быть от 1 до 6'''
    
    if not s.isdigit():
        return False
    
    amount = len(s)
    if amount < 2 or amount > 5:
        return False
    
    if s[-1] not in lust_nums.keys():
        return False
    return True

def is_cooret_value(val):
    '''Значение должно быть пробразуемо во float
    и значение должно быть от 0 до 6'''
    try:
        return 0 <= float(val) <= 6
    except:
        return False

def is_correct_num_answer(answer: str,amount: int) -> bool:
    '''Значение должно быть от 1 до amount'''
    
    try:
        return 1 <= int(answer) <= amount
    except:
        return False
