from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Fake database for now
USERS = {
    "admin@instasell.com": "admin123",
    "seller@test.com": "seller123"
}

@app.route('/')
def login_page():
    # Pehle login page dikhayenge
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
    return "Invalid Login! Dobara try karein."

@app.route('/admin')
def admin_dashboard():
    return render_template('index.html') # Jo abhi aapko dikh raha hai

@app.route('/dashboard')
def seller_dashboard():
    return "<h1>Seller Dashboard Coming Soon!</h1>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
