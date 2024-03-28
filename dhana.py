
from flask import Flask,render_template,url_for
import mysql.cnnector
app=Flask(__name__)   
mydb=mysql.connector.connect(host="localhost",user="root",password="system",db="blog13")
with mysql.connector.connect(host='localhost',password='system',user='root',db="blog13"):
    cursor=mydb.cursor(buffered=True)
    cursor.execute("cretae table if not exists additems(itemid varchar(30)primary key,name varchar(30),description varchar(20))")


@app.route('/')
def base():
    return render_template('homepage.html')

@app.route('/index')
def index():
    return "indexpage"

@app.route('/naveen/<int:num>')
def allow(num):
    return f"you allowed {str(num)}"

@app.route('/ifelse/<int:num>')
def ifelseprogram(num):
    if num>18:
        return "Right to vote"
    else:
        return "No Right to vote"
app.run(debug=True,use_reloader=True)









 
