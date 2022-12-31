import base64
from Crypto import Random
from Crypto.Cipher import AES

#adeuado de https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html
class AESCipher:

    def __init__(self, key):                                    
        self.key = bytes(key, 'utf-8')
        self.BS = 16

    def pad(self, s):
        _pad = bytes(s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS), 'utf-8')
        return _pad;

    def unpad(self, s):
        _unpad = s[0:-ord(s[-1:])];
        return _unpad

    def encrypt(self, raw):
        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:])).decode('utf8')

#el password siempre será 16 o multiplo
cipher = AESCipher('mysecretpassword')
encrypted = cipher.encrypt('frase a encriptar')
decrypted = cipher.decrypt(encrypted)

print(encrypted)
print(decrypted)
