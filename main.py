import ui
import storage
import asks


def main_loop():
    next_step = False
    
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
    main_loop()