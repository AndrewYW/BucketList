from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/bucketlist")
def bucket():
	return render_template('index.html')
@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')
@app.route("/signUp", methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate received values
    if _name and _email and _password:
	return json.dumps({'html':<span>all fields good</span>})
    else:
	return json.dumps({'html':<span>Enter required fields</span>})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
