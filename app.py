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

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    decrypted_text = ''
    if request.method == 'POST':
        encrypted = request.form.get('encrypted')
        private_key_input = request.form.get('private_key')

        try:
            # Convert PEM string to private key object
            private_key = serialization.load_pem_private_key(
                private_key_input.encode('utf-8'),
                password=None
            )

            # Decode Base64 and decrypt
            ciphertext = base64.b64decode(encrypted.encode('utf-8'))
            plaintext = private_key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            decrypted_text = plaintext.decode('utf-8')

        except Exception as e:
            decrypted_text = f"Error: {str(e)}"

    return render_template('decrypt.html', decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
