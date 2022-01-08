#user_id 預設空在page.htm裡面
from flask import Flask,render_template,url_for, redirect,request
from flask.sessions import NullSession
from xls import *
import os
is_log = 0 #0:未登入 1:學生 2:管理者
accountInfo = {"rowIndex" : 0} #dict [rowindex,]
entryCount = 0;
ENTRY_LIMIT = 5;

app = Flask(__name__)

@app.route("/")
def dir():
    global is_log, accountInfo, entryCount
    is_log = 0
    accountInfo = {"rowIndex" : 0} #dict [rowindex,]
    entryCount = 0;
    return redirect(url_for('page'))

@app.route('/log',methods=['POST','GET'])
def page():
    return render_template('page.htm')

@app.route('/log/student-page',methods=['POST','GET'])
def login1() :
    if loginAct(login(1)):
        return render_template('student-personal-information.htm')
    return redirect(url_for('page'))

@app.route('/log/manager-page',methods=['POST','GET'])
def login2() :
    if loginAct(login(2)):    
        return render_template("teacher-personal-information.htm")
    return redirect(url_for('page'))


def login(sheetItem):
    entryAllowed();
    print('id_userid')
    id = request.form.values('id_userid')
    if id == "" :
        return redirect(url_for('/log'))
    password = request.form.values('id_password')
    sheetName = xls.sheetName(sheetItem)
    is_log = 1 #xls.read(sheetName,id,password)
    sheetName = xls.sheetName(is_log)        
    if is_log != 0:
        return redirect(url_for('/'))

def loginAct(account):
    if account.is_log == 2:
        global accountInfo
        accountInfo = xls.Read(account.sheetName,id)
        return True
    return False

def entryAllowed():
    global entryCount
    entryCount += 1
    if entryCount > ENTRY_LIMIT : #登入過多 強制登出
        print("Too many login attempts. Please try later.")
        os.system("taskkill /im chrome.exe /f")
    
if __name__ == '__main__':
    app.debug = True
    app.run()

