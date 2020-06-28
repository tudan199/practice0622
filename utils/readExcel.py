import xlrd

def readExcel(path,row,col):
    """
    传入参数文件路径和行号、列号
    返回单元格的值
    """
    workbook=xlrd.open_workbook(filename=path)
    sheets=workbook.sheet_by_name('Sheet1')
    values = sheets.cell(row,col).value
    return values

if __name__=='__main__':
    keys=readExcel(r'C:\Users\eagle\Desktop\practise\practice0622\data\test.xls',0,0)
    print(keys)