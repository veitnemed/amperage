import storage
from datetime import date 
DATE_FORMAT = '%d %b'

def format_for_print_data(rows: list) -> list:
    format_rows = []
    for row in rows:
        new_row = []
        tottal_amp = 0
        serial, *amps, dt_iso = row
        
        new_row.append('№ '+ serial)
    

        for amp in amps:
            amp_round = str(round(float(amp),3)).rjust(4)
            new_row.append(amp_round)
            tottal_amp += float(amp)
        
        t = str(round(tottal_amp,3)).rjust(4)
        new_row.append(t) 
        date_obj = date.fromisoformat(dt_iso)
        date_format = date_obj.strftime(DATE_FORMAT).rjust(7)
        new_row.append(date_format)
        format_rows.append(new_row)
    return format_rows

def sorted_tottal(format_rows):
    return sorted(format_rows, key = lambda lst: float(lst[7].strip()), reverse=True)

def get_median(rows):
    freq800, freq1400, freq4900, freq5300, freq5500, freq5900 = [], [], [], [], [], []

    for line in rows:
        # защита от пустых/битых строк
        if len(line) < 8:
            continue

        ser, f8, f14, f49, f53, f55, f59, d = line
        freq800.append(float(f8))
        freq1400.append(float(f14))
        freq4900.append(float(f49))
        freq5300.append(float(f53))
        freq5500.append(float(f55))
        freq5900.append(float(f59))

    lenth = len(freq800)
    medians = ['Медиана:']
    tottal = 0.0

    # если данных нет (на всякий случай)
    if lenth == 0:
        medians += ['0'] * 6
        medians.append('0')
        return medians

    for line in (freq800, freq1400, freq4900, freq5300, freq5500, freq5900):
        s = sorted(line)
        mid = lenth // 2

        if lenth % 2 == 0:
            # n=2 -> mid=1 -> берем s[0] и s[1] (OK)
            med_val = (s[mid - 1] + s[mid]) / 2
        else:
            # n=1 -> mid=0 -> берем s[0] (OK)
            med_val = s[mid]

        tottal += med_val
        medians.append(str(round(med_val, 3)).rjust(4))

    medians.append(str(round(tottal, 3)).rjust(4))
    return medians


def get_mean(rows):
    tottal = 0.0
    freq800, freq1400, freq4900, freq5300, freq5500, freq5900 = [], [], [], [], [], []

    for line in rows:
        if len(line) < 8:
            continue
        ser, f8, f14, f49, f53, f55, f59, d = line
        freq800.append(float(f8))
        freq1400.append(float(f14))
        freq4900.append(float(f49))
        freq5300.append(float(f53))
        freq5500.append(float(f55))
        freq5900.append(float(f59))

    lenth = len(freq800)
    means = ['Среднее:']

    if lenth == 0:
        means += ['0'] * 6
        means.append('0')
        return means

    for line in (freq800, freq1400, freq4900, freq5300, freq5500, freq5900):
        s = sum(line) / lenth
        tottal += s
        means.append(str(round(s, 3)).rjust(4))

    means.append(str(round(tottal, 3)).rjust(4))
    return means

            
        
               

        
        
    
       