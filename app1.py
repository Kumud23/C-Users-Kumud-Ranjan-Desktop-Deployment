
from flask import Flask,render_template,request
from flask.signals import template_rendered
import joblib
# initialise the app
app=Flask(__name__)
model = joblib.load('dib_79.pkl')
print('[INFO] model loaded')

@app.route("/")
def hello_world():
    return render_template('home1.html')

@app.route('/predict' , methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    output = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    if output[0]==1:
        ans = 'dibatic'
    else:
        ans = 'not dibatic'
    return render_template('home1.html' , predict = f'the person is {ans}' )

app.run(debug=True)