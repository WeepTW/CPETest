// 參考資料 (https://ithelp.ithome.com.tw/articles/10213503) (https://www.youtube.com/watch?v=FWrdKjvJUaA)
#import excel
! pip install pandas
! pip install openpyxl
import pandas as pd
! pip install xlwt
! pip install xlrd
! pip install Flask 

from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/',methods=['POST'])

class xls:
    def read():
        df=pd.read_excel("filename.xlsx")
        pass

    def write():
        df['name'] = request.form['user_name']  //要從html的input抓取資料到xls裡面，但我不太確定
        df['class'] = request.form['user_class']  //同上
        df['student_ID'] = request.form['user_id']  //同上
        df['account_num'] = request.form['user_account']  //同上
        df['account_password'] = request.form['user_password']  //同上
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
