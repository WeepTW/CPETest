from flask import Blueprint, app,render_template,url_for, redirect,request
import xls

app = Blueprint('rounting', __name__)

@app.route('/student-page/<accountInfo>/<type>',methods=['POST','GET'])
def login1(accountInfo,type):
    if type ==  1:
        return render_template('student-personal-information.htm')
    return redirect(url_for('dir'))

@app.route('/manager-page/<accountInfo>/<type>',methods=['GET'])
def login2(accountInfo):
    accountInfo = eval(accountInfo)
    if type == 2 :
        return render_template("teacher-personal-information.htm")
    return redirect(url_for('dir'))

def loginAct(account):
    if account.is_log == 2:
        global accountInfo
        accountInfo = xls.Read(account.sheetName,id)
        return True
    return False

