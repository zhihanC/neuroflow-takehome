from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')

def home():
  return 'HOME PAGE: Go to the /verify endpoint to log in!'

@app.route('/verify', methods = ['GET', 'POST'])

def logIn():
  if request.method == 'POST':
    username = request.form.get("username") 
    password = request.form.get("password")
    if username == 'test' and password == 'test':
      return redirect(f'/mood')
    else:
      return render_template('form.html')
  else: 
    return render_template('form.html')

@app.route('/mood', methods = ["GET"]) 

def account():
  date = (0); 
  return render_template('userInfo.html', date = 0)
  
if __name__ == '__main__':
  app.run()