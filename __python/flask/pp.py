from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo1():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return "name: "+name

@app.route('/repeat/<times>/<name>')
def say2(times,name):
    str=" "
    for i in range (int(times)):
        str+="<p>"+name+"<p>"
    return str




if __name__=="__main__":
    app.run(debug=True) 
