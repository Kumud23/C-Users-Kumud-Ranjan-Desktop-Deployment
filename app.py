from flask import Flask,render_template,request
# initialise the app
app=Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('home.html')
@app.route('/hello')
def welcome():
    # return' welcome to home page'
    return render_template('home.html')

@app.route('/contact')
def contact():
    # return' welcome to contact page'
    return render_template('contact.html')
@app.route('/blog')
def blog():
    return' welcome to blog page'
@app.route('/gallery')
def gallery():
    return' welcome to gallery page'
@app.route('/details')
def details():
    return render_template('details.html')
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/geolocation')
def geolocation():
    return render_template('geolocation.html')



@app.route('/predict' , methods = ['post'])
def predict():
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')

    print(first_name)
    print(last_name)
    print(email)
    print(phone)

    return 'Form Submitted'

# run the app
app.run(debug=True)