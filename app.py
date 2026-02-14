from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Fake database for testing
USERS = {
    "admin@instasell.com": "admin123",
    "seller@test.com": "seller123"
}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_logic():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email in USERS and USERS[email] == password:
        if email == "admin@instasell.com":
            return redirect('/admin')
        else:
            return redirect('/dashboard')
    return "<h1>Invalid Login!</h1><p>Email ya password galat hai. <a href='/'>Wapas jayein</a></p>"

@app.route('/admin')
def admin_dashboard():
    return render_template('index.html')

@app.route('/dashboard')
def seller_dashboard():
    return "<h1>Seller Dashboard Coming Soon!</h1><p>Bhai, seller ka kaam abhi baaki hai.</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
