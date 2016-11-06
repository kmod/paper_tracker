from flask import render_template, request, redirect

from app import app
from model import db, Paper

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/paper/new', methods=["GET", "POST"])
def paper_new():
    if request.method == "GET":
        return render_template("paper_new.html")
    else:
        assert request.method == "POST"
        print request.form
        p = Paper(title=request.form['title'])
        db.session.add(p)
        db.session.commit()
        return redirect('/paper/' + str(p.id))
    return "Unknown method " + request.method

@app.route('/paper/<int:id>')
def paper(id):
    p = Paper.query.get(id)
    if not p:
        return "Paper %d not found" % id
    return p.title
