from flask import Flask,render_template,request,redirect
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
import DateTime


app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db=SQLAlchemy(app)
class todouu(db.Model):
    todo_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title=db.Column(db.Text)
    des=db.Column(db.Text)
    date=db.Column(db.DateTime,server_default=db.func.now())


with app.app_context():
    db.create_all()


@app.route("/hello")
def hi():
      data=todouu.query.all()
      #print(data)
      return render_template("hello.html",mdata=data)




@app.route("/savedata",methods=["POST"])
def datasaving():
    if request.method=="POST":
        title=request.form.get("title")
        desc=request.form.get("des")
        page=todouu(title=title,des=desc,)

        db.session.add(page)
        db.session.commit()

        return redirect("/hello")

    return "data saved"



@app.route ("/deletethisdate/<int:yz>")
def deletethisnow(yz):
    data=todouu.query.get(yz)
    db.session.delete(data)
    db.session.commit()
   
    return redirect("/hello")

@app.route("/update/<int:abc>")
def updatethis(abc):
    data=todouu.query.get(abc)
    return render_template("hello.html")


@app.route("/updatedatanow/<int:abc>",methods=["POST"])
def updatethisu(abc):
        data=todouu.query.get(abc)
        if request.method=="POST":
            title=request.form.get("title")
            desc=request.form.get("des")
            data.title = title
            data.desc = desc
            
            db.session.commit()
            return redirect("/hello")
 


if __name__=="__main__":
    app.run(port=5000,debug=True)