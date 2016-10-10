from flask import Flask, render_template
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
if __name__ == "__main__":
    app.run(host='0.0.0.0')
