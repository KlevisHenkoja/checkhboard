from flask import Flask, render_template, redirect
app = Flask(__name__)   
@app.route('/<int:x>/<int:y>')
def checkbord1(x,y):
    return render_template('list.html', gjatesia=x, gjeresia=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkbord2(x,y, color1, color2):
    return render_template('list.html', gjatesia=x, gjeresia=y, color1=color1, color2=color2)


if __name__=="__main__":   
    app.run(debug=True) 

