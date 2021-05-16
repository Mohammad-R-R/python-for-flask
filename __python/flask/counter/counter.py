from flask import Flask, app, session,render_template,redirect


app =Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def count():
    session['counter']=0
    return redirect("/count")

@app.route("/count")
def add_counter():
    count=session['counter']
    count=count+1
    session['counter']=count
    return render_template("counter.html",count=session['counter'])

@app.route("/destroy_session")
def clear():
    session.clear()
    return redirect('/')

@app.route("/add_two")
def add():
    session['counter']+=2
    return render_template("counter.html",count=session['counter'])





if __name__=="__main__":
    app.run(debug=True)







