import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher:
    """
    inspirado en
    https://bit.ly/3uNfbBM
    https://bit.ly/3Rsvgqx
    https://bit.ly/3IE1ue5
    """

    def __init__(self, key):
        #la variable key puede tener una cantidad variable sin embargo private_key tendrá multiplos permitidos
        # self.key = bytes(key, 'utf-8')
        # private_key tendrá 16 caracteres o su multiplo
        self.private_key = hashlib.sha256(key.encode("utf-8")).digest();
        self.BS = 16

    def pad(self, s):
        _pad = bytes(s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS), 'utf-8')
        return _pad;

    def unpad(self, s):
        _unpad = s[0:-ord(s[-1:])];
        return _unpad

    def encrypt(self, plain_text):
        plain_text = self.pad(plain_text)
        print("After padding:", plain_text)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(plain_text))

    def decrypt(self, cipher_text):
        cipher_text = base64.b64decode(cipher_text)
        iv = cipher_text[:16]
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(cipher_text[16:])).decode('utf8')


#el password res variable
cipher = AESCipher('mypassword')
encrypted = cipher.encrypt('frase a encriptar')
decrypted = cipher.decrypt(encrypted)

print(encrypted)
print(decrypted)
