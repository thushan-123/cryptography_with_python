from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# generate key pair
key = RSA.generate(3072)

pub_key = key.public_key()

pub_key_pem = pub_key.export_key()

pri_key_pem = key.export_key()

print("----Asymmetric-Encryption----")

text = input("Enter a plain text: ")

# encryption
encryptor = PKCS1_OAEP.new(pub_key)
encrypted = encryptor.encrypt(text.encode())
                              
print("Encrypted:", binascii.hexlify(encrypted))

# decryption
decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(encrypted)
print("Decrypted:", decrypted.decode())
