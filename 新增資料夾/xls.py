#import excel
! pip install pandas
! pip install openpyxl
import pandas as pd
! pip install xlwt
! pip install xlrd
! pip install Flask 

from flask import Flask,render_template,request
import xlwt
app=Flask(__name__)
@app.route('/',methods=['POST'])

class xls:
    def read():
        df=pd.read_excel("filename.xlsx")
        pass

    def write():
        df['name'] = request.form['user_name']
        df['class'] = request.form['user_class']
        df['student_ID'] = request.form['user_id']
        df['account_num'] = request.form['user_account']
        df['account_password'] = request.form['user_password']
        pass

    def nameCheck():
        pass

    def sheetName(is_log):
        if is_log == 1:
            return "學生"
        if is_log == 2:
            return "管理者"
        else:
            return ""
