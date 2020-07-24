from flask import Flask
from flask import request,render_template,redirect,url_for
import mysql.connector
import sqlite3
import pymysql
#mydb = sqlite3.connect('identifier.sqlite')
mydb = pymysql.connect(host="https://drive.google.com/file/d/1WZL_LrvEMgqJJg_hkGPGp5Y6uyiYPN0t/view?usp=drivesdk",database="identifier.sqlite",user="manohar",passwd="9618287133")

mycursor = mydb.cursor()


# ...
app = Flask(__name__)
@app.route('/')
def home():
  return render_template("login.html")
@app.route('/reg')
def reg():
    return render_template("reg.html")
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        name=request.form['name']
        passw=request.form['psw']


        #mydb = sqlite3.connect('identifier.sqlite')
        mydb = pymysql.connect(host="database-1.c4i4uil4h10w.us-east-2.rds.amazonaws.com", database="solo", port=3306,
                               user="manohar", passwd="9618287133")

        mycursor = mydb.cursor()
        #mycursor.execute("create table run(id int,name )"
        mycursor.execute("select * from run")
        c = mycursor.fetchall()
        print(c)
        for row in c:
            print(row)
        mycursor.execute("insert into run(id,name) values(1,'manu')")
                         #,(name,passw))
        mydb.commit()
        mydb.close()
        return redirect(url_for('reg'))
    return render_template("login.html")
if __name__ == "__main__":
    app.run()
