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
        ser, f8, f14, f49, f53, f55, f59, d = line
        freq800.append(float(f8))
        freq1400.append(float(f14))
        freq4900.append(float(f49))
        freq5300.append(float(f53))
        freq5500.append(float(f55))
        freq5900.append(float(f59))
    lenth = len(freq800)
    medians = ['Медиана:']
    tottal = 0
    for line in (freq800, freq1400, freq4900, freq5300, freq5500, freq5900):
        s = sorted(line)
        if lenth % 2 == 0:
            idx = int(lenth/2)
            med_val = (s[idx] + s[idx+1])/2
        else:
            idx = int((lenth+1)/2)
            med_val = s[idx]
        tottal += med_val
        t = str(round(med_val,3)).rjust(4)
        medians.append(t)
    medians.append(str(round(tottal,3)).rjust(4))
    return medians

def get_mean(rows):
    tottal = 0
    freq800, freq1400, freq4900, freq5300, freq5500, freq5900 = [], [], [], [], [], []
    for line in rows:
        ser, f8, f14, f49, f53, f55, f59, d = line
        freq800.append(float(f8))
        freq1400.append(float(f14))
        freq4900.append(float(f49))
        freq5300.append(float(f53))
        freq5500.append(float(f55))
        freq5900.append(float(f59))
    lenth = len(freq800)
    means = ['Среднее:']

    for line in (freq800, freq1400, freq4900, freq5300, freq5500, freq5900):
        s = sum(line)/lenth
        tottal += s
        t = str(round(s,3)).rjust(4)
        means.append(t)
    means.append(str(round(tottal,3)).rjust(4))
    return means


            
        
               

        
        
    
       