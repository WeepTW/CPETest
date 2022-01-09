#user_id 預設空在page.htm裡面
from flask import Flask,render_template,url_for, redirect,request,Blueprint
import xls,os
import log
import rounting

accountInfo = {"rowIndex" : 0} #dict [rowindex,]
entryCount = 0;
ENTRY_LIMIT = 5;

app = Flask(__name__)
app.register_blueprint(log.app,url_prefix='/log',template_folder='templates')
app.register_blueprint(rounting.app,url_prefix='/log',template_folder='templates')

@app.route("/")
def dir():
    global is_log, accountInfo, entryCount
    is_log = 0
    accountInfo = {"rowIndex" : 0} #dict [rowindex,]
    entryCount = 0;
    return redirect(url_for('log.page'))

def hasAccount(sheetName,id,password):
    #pass
    return {"rowIndex" : 1, "id" : 410731220, "name" : "水獺狗"}

app.debug = False
if __name__ == '__main__':
    app.debug = False
app.run()
