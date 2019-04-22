import xlrd

wb = xlrd.open_workbook('data.xlsx')
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))
print('-----------------------------')

print('Dispaying value from Cell:'+ sheet.cell_value(0,0))
print(sheet.nrows)
print('2nd row value------------------------')
print(sheet.row_values(1))

print('All Rows: -----------------------------')
row_count = sheet.nrows
for i in range(row_count):
    print(sheet.row_values(i))

print('All Columns:----------------------------')
col_count = sheet.ncols
for i in range(col_count):
    print(sheet.col_values(i))