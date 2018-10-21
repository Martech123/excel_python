import xlrd
import xlwt
from xlutils.copy import copy

data = xlrd.open_workbook("ATEST.xlsx")
table = data.sheet_by_name("ATEST")
write_data = copy(data)
write_table = write_data.get_sheet(0)
nub_rows = table.nrows
nub_cols = table.ncols

col_te = table.col_values(0)
for nub_row in range(0, nub_rows):
    string = col_te[nub_row].encode("utf-8")
    new_string = filter(str.isdigit, string)
    #new_string.replace(' ', '')
    #new_new_string = new_string.rstrip()
    if new_string:    
        print(new_string)
        write_table.write(nub_row, 5, new_string)
        write_data.save("TEST.xls")


#colnames = table.row_values(2)
#list = []
#
#for i in range(0, nub_rows):
#    row = table.row_values(i)
#    if row:
#        for s in range(len(colnames)):
#            app = {}
#            app[colnames[s]] = row[s]
#            list.append(app)


#for m in range(len(list)):
#    print(list[m])
