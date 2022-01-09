
from flask import Blueprint, render_template,url_for, redirect,request
import xls,app,json
ENTRY_LIMIT = 5
entryCount = 0
is_log = 1 # 0:Null 1:student 2:manager

def loginAct(sheetName,id,password):
    global is_log
    accountInfo = xls.read(id, password) #list of accountInfo
    is_log = xls.sheetName(sheetName)
    if accountInfo["rowIndex"] > 1:
        with open('templates/static/tmp.json', 'wb') as fp:
            fp = dump_json(accountInfo)
        json.dumps(accountInfo) #網頁暫存
        if is_log == "管理者" :
            return 2
        if sheetName == "學生":
            return 1
    is_log = 0
    return 0
    #render_template('student-personal-information.htm',accountInfo = accountInfo)

def entryLimit():
    global count
    if count >= ENTRY_LIMIT :
        count += 1
    else:
        app.fail()

def initEntry():
    global count
    count = 0
    return

#by https://medium.com/seaniap/python-web-flask-%E5%B0%8Djson%E7%9A%84%E5%AD%98%E5%8F%96-1-69a330ce59aa
def dump_json(dic_data):
    j_file = json.dumps(dic_data, indent=2)
    print(f'Wiil output: {j_file}')
    return j_file