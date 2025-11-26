from Crypto.Cipher import AES
import base64
import argparse

secret_key = b'thoe8j0l3&123456'  

iv = b'1234567890abcdef'          

def encryption(plain_text):
    cipher = AES.new(secret_key, AES.MODE_CFB, iv=iv)
    cipher_text = cipher.encrypt(plain_text.encode())

    print(base64.b64encode(cipher_text).decode())

def decryption(cipher_text):
    cipher = AES.new(secret_key, AES.MODE_CFB, iv=iv)
    decrypted = cipher.decrypt(base64.b64decode(cipher_text))
    
    print(decrypted.decode())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Symmetric Encryption and Decryption')

    parser.add_argument('-e', '--encrypt', help='enter plain text')
    parser.add_argument('-d', '--decrypt', help='enter cipher text')

    args = parser.parse_args()

    if args.encrypt:
        encryption(args.encrypt)
    elif args.decrypt:
        decryption(args.decrypt)

    
