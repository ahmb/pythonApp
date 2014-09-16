from flask import *
from functools import wraps
#Flask, render_template
#initialize the instance according to the WSGI rules
app = Flask(__name__)

#make sure the key is completely randomized sequence of letters and numbers
app.secret_key = 'my precious'

@app.route("/")
def home():
    return render_template('home.html')
	
@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route('/logout')	
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect (url_for('log'))

	
@app.route("/hello")
def hello():
    return render_template('hello.html')
	
@app.route("/log", methods=['GET', 'POST'])
def log():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('hello'))
	return render_template('log.html', error=error)
	
def hello():
    return "Hello World!"

if __name__ == "__main__":
    #app.debug() = True
    app.run(debug=True)

    app.run()
    
