import openpyxl
import os
os.getcwd() # 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64'
os.chdir('d:\\users\\trent\\desktop\\ATBSWP')

workBook = openpyxl.load_workBook(example.xlsx)
wb = workBook
wb = openpyxl.workbook.Workbook.sheetnames()


