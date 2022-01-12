#page student & manager must set.localStorage(accountInfo) 
from flask import Flask,render_template,url_for, redirect,request,jsonify
import xls,view,json

app = Flask(__name__)

#app

@app.route("/")
def dir():
    view.initEntry()
    return redirect(url_for('page'))

@app.route('/log/tmp', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form.get('userid') == '1' and request.form.get('password') == '1':
            type = 1
        elif request.form.get('sheetName') == 2:
            type = 2
        else :
            type = 0
        # type = view.loginAct(request.form.get('sheetName') ,request.form.get('userid'),request.form.get('password')) #回傳accountInfo的json
        if type == 1:
            return redirect(url_for('loginSt'))
        elif type == 2:
            return redirect(url_for('loginMa'))
        else:
            return redirect(url_for('page'))
    else:
        print('預設帳密是 1 1 ')
        return redirect(url_for('page'))

#route

@app.route('/log')
def page():
    return render_template('page.htm')

@app.route('/log/student-page', methods = ['GET'])
def loginSt():
    if view.is_log == 1:
        return render_template('student-personal-information.htm')
    else:
        return redirect(url_for('page'))


@app.route('/log/teacher-page', methods = ['POST'])
def loginTa(type,item):
    view.is_log = 2 #資料庫新增後要更改為call-change
    if view.is_log == 2:
        view.teacher(request.form.get('typeOf'),request.form.get('obj'))
        return render_template("teacher-personal-information.htm")
    else:
        return redirect(url_for('page'))

@app.route('/log/student/tmp/<type>', methods = ['POST','GET'])
def tmpSt(type):
    if request.method == 'GET' and view.is_log == 1:
        type = int(type)
        if type == 1:
            return redirect(url_for('loginSt'))
        elif type == 2:
            return render_template('student-personal-information-change.htm')
        elif 300 < type < 403 :
            return render_template('student-exercise' + str(type % 300) + '.htm')
        elif 400 < type < 500:
            return render_template('student-exem' + str(type % 400) + '.htm')
        elif type == 5:
            return render_template('student-exercise-score.htm')
        elif type == 52:
            return render_template('student-exem-score.htm')
        else:
            return redirect(url_for('page'))
    else:
        return redirect(url_for('dir')) 

@app.route('/log/teacher/tmp', methods = ['GET'])
def tmpTa(type,item):
    if request.method == 'GET' and view.is_log == 2:
        type = int(type)
        if type == 1:
            return redirect(url_for('loginTa'))
        elif type == 2:
            return render_template('teacher-personal-information-change.htm')
        elif 200 < type < 300 :
            return render_template('待更新') #('teacher-exercise' + str(type % 100) + '.htm')
        elif type == 4:
            return render_template('teacher-exem-score.htm')
        elif type == 5:
            return render_template('teacher-exam-change.htm')
        else:
            return redirect(url_for('page'))
    else:
        return redirect(url_for('dir'))

@app.route('/fail')
def fail():
    return redirect(url_for('fail')) #失敗頁面

if __name__ == '__main__':
    app.run(debug = False)

