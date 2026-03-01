import ui
import storage
import asks
import locale
import analytics as anl

def show_rows():
    data = storage.get_data()
    format_data = anl.format_for_print_data(data)
    ui.show_all_rows(format_data)
    medians = anl.get_median(data)
    tit, f1, f2, f3, f4, f5, f6, f = medians
    print(f'  {tit}     | {f1}   | {f2}   | {f3}   | {f4}   | {f5}   | {f6}   |  {f}   | -------- |  ')
    means = anl.get_mean(data)
    print('==========================================================================================|')
    tit, f1, f2, f3, f4, f5, f6, f = means
    print(f'  {tit}     | {f1}   | {f2}   | {f3}   | {f4}   | {f5}   | {f6}   |  {f}   | -------- |  ')



def local_time():
    try:
       locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    except:
        pass 

def main_loop():
    local_time()
    storage.ensure_file()
    ui.clean_terminal()
    
    while True:
        ui.show_tittle()
        ui.show_post_tittlee()
        
        row = asks.get_csv_row()
        storage.write_row(row)
        ui.complete_write(row[0],asks.get_factories_in_full(row[0]))
        next_step = asks.is_next_step()
        if next_step:
            continue
        else:
            break
    ui.clean_terminal()
        
        
    

if __name__ == '__main__':
    show_rows()
    