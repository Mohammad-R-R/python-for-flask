from flask import Flask, render_template, request, redirect 

app = Flask(__name__)
@app.route('/')            
def thestyle():
    return render_template("dojoser.html")  
@app.route('/show',methods=['POST'])          
def thepoint():
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    text=request.form['text']
    return render_template("show.html",name=name,location=location,language=language,text=text)  

    
if __name__=="__main__":     
    app.run(debug=True)    