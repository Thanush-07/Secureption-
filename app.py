from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt')

def encrypt():
    return render_template('encrypt.html')

@app.route('/decrypt')

def decrypt():
    return render_template('decrypt.html')

@app.route('/instruction')

def instruction():
   return render_template('instruction.html')


if __name__ == '__main__':
    app.run(debug=True)
