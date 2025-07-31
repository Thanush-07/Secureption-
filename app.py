from flask import Flask, render_template, request
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt')
def encrypt():
    return render_template ('encrypt.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/instruction')
def instruction():
    return render_template('/instruction.html')
if __name__ == '__main__':
    app.run(debug=True)
