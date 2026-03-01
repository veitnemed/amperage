import csv

COLUMNS = ['0.8','1.4','4.9','5.3','5.5','5.9']
FILE_NAME = 'AMPERAGE.csv'

def load_data() -> list:
    try:
        with open(FILE_NAME,'w', encoding='urf-8') as file:
            reder_obj = list(csv.reader(file))[1:]
            if len(reder_obj) > 0:
                return reder_obj
            else:
                return []   
    except:
        with open(FILE_NAME,'w', encoding='urf-8', newline=''):
            writer_obj = csv.writer(file)
            writer_obj.writerow(COLUMNS)
            return []