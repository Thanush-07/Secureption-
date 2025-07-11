📖 Project Explanation

Secureption  is a web-based encryption and decryption tool that implements the **RSA asymmetric encryption algorithm** using Python and Flask. The main goal of this project is to help users understand how public-key cryptography works through a simple and interactive interface.

Unlike traditional symmetric encryption where the same key is used to both encrypt and decrypt data, RSA uses a **pair of keys**:

* A **public key** that is shared and used to  encrypt messages
* A **private key** that is kept secret and used to  decrypt messages

The application allows users to:

* 🔐 **Generate secure RSA key pairs** (2048-bit strength)
* 📥 **Encrypt plaintext messages** using the public key
* 📤 **Decrypt encrypted messages** using the private key
* 📄 **Work with Base64 output**, making ciphertext easy to copy and share

Secureption is designed with beginners, students, and security enthusiasts in mind. It provides a practical understanding of:

* How **secure message transmission** works
* The concept of **key management**
* The basics of **cryptographic padding (OAEP with SHA-256)**

The backend uses Python’s `cryptography` library to ensure secure and proper implementation of encryption standards. The frontend is powered by Flask and provides a simple web interface where users can test encryption without needing to write any code.

Whether you're a cybersecurity student, a developer experimenting with cryptography, or just curious about how encryption protects your data — **Secureption** is a great tool to learn, test, and explore.



