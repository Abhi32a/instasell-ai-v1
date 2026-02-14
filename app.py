from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Ye automatic templates folder ke andar index.html ko dhoondega
    return render_template('index.html')

if __name__ == '__main__':
    # Render ke liye dynamic port setup
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
