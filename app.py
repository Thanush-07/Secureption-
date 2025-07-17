from flask import Flask, render_template, request
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    encrypted_text = ''
    if request.method == 'POST':
        # Get message and public key from form
        message = request.form.get('plaintext')
        public_key_input = request.form.get('public_key')

        try:
            # Load the public key from PEM format
            public_key = serialization.load_pem_public_key(
                public_key_input.encode('utf-8')
            )

            # Encrypt the message using OAEP padding
            ciphertext = public_key.encrypt(
                message.encode('utf-8'),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            # Encode encrypted bytes to base64 string
            encrypted_text = base64.b64encode(ciphertext).decode('utf-8')

        except Exception as e:
            encrypted_text = f"Error: {str(e)}"

    return render_template('encrypt.html', encrypted_text=encrypted_text)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/decrypt')
def decrypt():
    return render_template('decrypt.html')

@app.route('/instruction')
def instruction():
    return render_template('instruction.html')

if __name__ == '__main__':
    app.run(debug=True)
