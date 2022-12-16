from flask import Flask
from flask import render_template,redirect,flash,url_for
from flask import request,make_response,session,Response
from adminsettings import *
app = Flask(__name__)
#app.config["SCRECT-KEY"]= 996000
@app.route('/')
def index():
  return render_template("home.html")
  
@app.route('/classes')
def classes():
  User.init()
  return render_template("classes.html",name= User.name)
  
@app.route('/mine')
def mine():
  try :
    name= request.cookies.get("UserName")
    if not name:
      return redirect("/login")
    else:
      User.init()
    
    
      admin= {"name":name,
              "password":User.menber[name]
             }
      return render_template("mine.html",admin=admin )
  except:
    resp= make_response(redirect("/mine"))
    Response.delete_cookie(resp,"UserName")
    return resp
@app.route('/login',methods= ["POST","GET"])
def login():
  if request.method==  "POST":
    User.init()
    nm= request.form.get("name")
    pw= request.form.get("password")
    print(nm,pw)
    admin= User(nm,pw )
    if not admin.if_in():
      alert= "没有此账号，请注册"
      return render_template("register.html",alert= alert)
    elif not admin.check():
      alert= "输入不合法！请重新输入！"
      return render_template("login.html",alert= alert)
    elif not admin.true_pw():
      alert= "密码错误!"
      return render_template("login.html",alert= alert)
    else:
      #admin.log()
      resp= make_response(render_template("mine.html",admin= {
        "name":nm,
        "password":pw
      }) )
      resp.set_cookie("UserName",admin.name,max_age= 10*24*60*60*1000)
      
      return resp
  else :
    alert= "目前没有登录账号，请登录账号!"
    return render_template("login.html",alert= alert)

@app.route('/register',methods= ["POST","GET"])
def register():
  if request.method==  "POST":
    User.init()
    nm= request.form.get("name").replace(" ","")
    pw= request.form.get("password")
    pw_=request.form.get("password_")
    admin= User(nm,pw )
    if admin.if_in():
      alert= "该账号已被注册!"
      return render_template("register.html",alert= alert)
    elif not admin.check():
      alert= "输入不合法!"
      return render_template("register.html",alert= alert)
    elif not pw== pw_:
      alert= "再次输入错误"
      return render_template("register.html",alert= alert)
    else:
      admin.rgst()
      User.save()
      resp= make_response(render_template("mine.html",admin= {
        "name":nm,
        "password":pw
      }) )
      resp.set_cookie("UserName",admin.name,max_age= 10*24*60*60*1000)
      return resp
  else :
    alert= "注册一下账号 "
    return render_template("register.html",alert= alert)

@app.route("/delog")
def delog():
  try:
    resp= make_response(render_template("login.html",alert= "退出成功!") )
    Response.delete_cookie(resp,"UserName")
    return resp
  except:
    return "我们遇到一个错误，请重试"

@app.route("/deuser")
def deuser():
  try:
    resp= make_response(render_template("register.html",alert= "注销成功!"))
    User.init()
    del User.menber[request.cookies.get("UserName")]
    User.save()
    Response.delete_cookie(resp,"UserName")
    return resp
  except:
    return "我们遇到一个错误,请重试"
app.run(host='0.0.0.0', port=81,debug= True)

