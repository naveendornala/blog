from flask import Flask,render_template,url_for,request,redirect,url_for
import mysql.connector
from cmail import sendmail
from otp import genotp
app=Flask(__name__)   
mydb=mysql.connector.connect(host="localhost",user="root",password="system",db="blog13")
with mysql.connector.connect(host='localhost',password='system',user='root',db="blog13"):
    cursor=mydb.cursor(buffered=True)
    cursor.execute("create table if not exists registration(username varchar(50) primary key,mobile varchar(20) unique,email varchar(50)unique,address varchar(50), password varchar(20))")



@app.route("/form",methods=['GET','POST'])
def base():
    if request.method=='POST':
        
        username=request.form.get('username')
        mobile=request.form.get('mobile')
        email=request.form.get('email')
        address=request.form.get('address')
        password=request.form.get('password')
        cursor=mydb.cursor(buffered=True)
        cursor.execute('insert into registration values(%s,%s,%s,%s,%s)',[username,mobile,email,address,password])
        mydb.commit()
        cursor.close()
        return redirect(url_for("login"))
    return render_template("registration.html")
@app.route('/login')
def login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select count(*) from registration where username=%s && password=%s',[username,password])
        data=cursor.fetchone()[0]
        print(data)
        if data==1:
            return redirect(url_for('homepage'))
        else:
            return "Invalid Username and password"
    return render_template("login.html")
@app.route('/')
def homepage():
    return "homepage"
app.run()



