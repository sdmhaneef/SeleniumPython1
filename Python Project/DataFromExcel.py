
# Program to extract a particular row value
import xlrd

loc = ("C:\Users\Allah\Desktop\Data.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)
print sheet.cell_value(1, 0)
print sheet.cell_value(1, 1)

print(sheet.row_values(1))
