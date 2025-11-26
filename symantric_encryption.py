from Crypto.Cipher import AES
import base64
import argparse

secret_key = b'thoe8j0l3&123456'

cipher = AES.new(secret_key,AES.MODE_CFB)

# plain text


def encryption(palin_text):
    cipher_text = cipher.encrypt(plain_text.encode())
    print(base64.b64encode(cipher_text))

def decryption(cipher_text):

    print(cipher.decrypt(base64.b64decode(cipher_text)).decode())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Symantric Encryption and Decryption')

    parser.add_argument('-e', '--encrypt', help='enter plain text')
    parser.add_argument('-d', '--decrypt', help='enter cipher text')
    
