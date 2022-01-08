from flask import Flask,render_template,url_for, redirect,request
from flask.sessions import NullSession
from .xls import *

global is_log #1:學生 2:管理者
global accountInfo #dict [rowindex,]

app = Flask(__name__)

@app.route("/")
def dir():
    is_log = 0
    accountInfo = {"rowIndex" : 0}
    return redirect(url_for('log'))

@app.route('/log',methods=['POST','GET'])
def page():

    return render_template('page.html')

@app.route('/log/student-page',methods=['POST','GET'])
def login1() :
    account = login()
    if account.is_log == 1 :
        global is_log
        is_log = 1
        accountInfo = xls.Read(account.sheetName,id)
        return redirect(url_for('/student'))
    return redirect(url_for('log'))

@app.route('/log/manager-page',methods=['POST','GET'])
def login1() :
    account = login()
    if account.is_log == 2:
        accountInfo = xls.Read(account.sheetName,id)
        return redirect(url_for('/manager'))
    return redirect(url_for('log'))

def QQ(id,password):
    pass

    return 0


class login:
    def __str__(self):
        id = request.form.values('user_id')
        password = request.form.values('user_password')
        is_log = xls.nameCheck(type,id,password)
        sheetName = xls.sheetName(is_log)
        
        elif is_log != 0:
            return redirect(url_for('/'))
        return NullSession


"""
@app.route('/student')
def student(is_log):
    if is_log == 1:
        return render_template('student-page.html')
    else:

        //讀取excel整串
        accountInfo = { //dict
            rowIndex = ?
            ...

        }
        return redirect(url_for('log'),accountInfo = accountInfo)

@app.route('/manager')
def manager(is_log):
    if is_log == 2:
        return render_template('manager-page.html')
    else:
        return redirect(url_for('log'))
"""
