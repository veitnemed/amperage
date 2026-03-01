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
       