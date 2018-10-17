
import csv
import xlrd
import sys
from pprint import pprint


def read_excel(filename):
    """Returns a nested list with the contents of an Excel table."""
    data = []

    workbook = xlrd.open_workbook(filename)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])

    for row_idx in range(0, sheet.nrows):
        row = []
        for col_idx in range(0, sheet.ncols):
            cell_obj = sheet.cell(row_idx, col_idx)
            row.append( cell_obj )
        data.append(row)
    return data


xls_filename = sys.argv[1]

data = read_excel(xls_filename)

pprint(data)

writer = csv.writer(open('output.txt', 'w'), delimiter='|')
writer.writerows(data)


