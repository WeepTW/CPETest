
from flask import Blueprint,render_template,url_for, redirect,request
import xls
import rounting
import app as home

def init():
    global _is_log #0:未登入 1:學生 2:管理者
    _is_log = 0
app = Blueprint('log', __name__)
init()

@app.route('/',methods=['POST','GET'])
def page():
    
    return render_template('page.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if True: #request.method == 'Post':
        sheetName = request.form.get('sheetName')
        accountInfo =  xls.read(sheetName,request.form.get('userid'),request.form.get('password'))
        if accountInfo["rowIndex"] > 1:
            if sheetName == "管理者" :
                return redirect(url_for('rounting.login2'),accountInfo = accountInfo, type = 1,action='GET')
            if sheetName == "學生":
                return redirect(url_for('rounting.login1'),accountInfo = accountInfo,type = 2,action='GET')
    return redirect(url_for('log.page'))


