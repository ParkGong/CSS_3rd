from openpyxl import *

def get_rawdata_from_excel(filename):
    '''
    get_rawdata_from_excel(filename) -> dict of rawdata
    엑셀에서 파일을 읽어와서 {'name' : score', ...}의 딕셔너리를
    반환한다 
    '''
    wb = load_workbook(filename)
    ws = wb.active

    raw_data = {}

    g = ws.rows

    for c1, c2 in g:
        raw_data.update({c1.value : c2.value})
    return raw_data
