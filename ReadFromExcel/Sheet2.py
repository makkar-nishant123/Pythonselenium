import xlrd

wb = xlrd.open_workbook('data.xlsx')
sheet2 = wb.sheet_by_index(1)
sheet2.cell_value(0,0)

for i in range(sheet2.ncols):
    print(sheet2.cell_value(0,i))
print('-----------------------------')

print('Dispaying value from Cell:'+ sheet2.cell_value(0,0))
print(sheet2.nrows)
print('2nd row value------------------------')
print(sheet2.row_values(1))

print('All Rows: -----------------------------')
row_count = sheet2.nrows
for i in range(row_count):
    print(sheet2.row_values(i))

print('All Columns:----------------------------')
col_count = sheet2.ncols
for i in range(col_count):
    print(sheet2.col_values(i))