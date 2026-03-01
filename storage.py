import csv
from pathlib import Path

HEADER = ['serial','0.8','1.4','4.9','5.3','5.5','5.9','date iso']

DATA_DIR = Path(r"C:\amperage_dir")
FILE_PATH = DATA_DIR / "AMPERAGE.csv"


def file_exists() -> bool:
    """True если файл есть"""
    return FILE_PATH.exists()


def create_columns() -> None:
    """Создать папку (если нет) + перезаписать файл заголовком"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(FILE_PATH, 'w', encoding='utf-8', newline='') as f:
        csv.writer(f).writerow(HEADER)


def ensure_file() -> None:
    """Создает папку, создает файл, чинит заголовок (с сохранением данных)."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # файла нет
    if not file_exists():
        create_columns()
        return

    # читаем как есть
    with open(FILE_PATH, 'r', encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f))

    # файл пустой
    if not rows:
        create_columns()
        return

    # заголовок битый -> перезаписать заголовок, данные сохранить
    if rows[0] != HEADER:
        with open(FILE_PATH, 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            w.writerow(HEADER)
            w.writerows(rows[1:])


def get_all_data() -> list:
    """Вернуть все строки (включая заголовок)"""
    ensure_file()
    with open(FILE_PATH, 'r', encoding='utf-8', newline='') as f:
        return list(csv.reader(f))


def get_data() -> list:
    """Только данные (без заголовка)"""
    rows = get_all_data()
    return rows[1:] if len(rows) > 1 else []


def get_len_file() -> int:
    """Длина файла (включая заголовок)"""
    return len(get_all_data())


def get_len_data() -> int:
    """Количество строк данных"""
    return len(get_data())


def has_only_header() -> bool:
    """Нет записей"""
    return get_len_data() == 0


def has_data() -> bool:
    """Есть хотя бы одна запись"""
    return get_len_data() > 0


def sys_write_row(row: list) -> None:
    """Дописать одну строку БЕЗ проверок"""
    with open(FILE_PATH, 'a', encoding='utf-8', newline='') as f:
        csv.writer(f).writerow(row)


def write_row(row: list) -> None:
    """Безопасная запись: ensure -> append"""
    ensure_file()
    sys_write_row(row)