import base64, hashlib, sys, time, os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# main.py
# Date: 01/02/2022
# Author: execution
# Contributor: therealOri


class C0mptCrypt:

    def __init__(self):
        self.hash_key = hashlib.blake2b("c0mpt0_&_Ori".encode('utf-8'), digest_size=16).digest()

    def Clear(self):
        os.system('clear||cls')

    def EncryptSpinner(self):
        l = ['|', '/', '√', '\\']
        for i in l+l+l:#
            sys.stdout.write(f'\rEncrypting...'+i)
            sys.stdout.flush()
            time.sleep(0.2)

    def DecryptSpinner(self):
        l = ['|', '/', '√', '\\']
        for i in l+l+l:#
            sys.stdout.write(f'\rDecrypting...'+i)
            sys.stdout.flush()
            time.sleep(0.2)

    def Encrypt(self, string):
        r = get_random_bytes(AES.block_size)
        h = AES.new(self.hash_key, AES.MODE_CBC, r)
        e = base64.b64encode(r + h.encrypt(pad(string.encode('utf-8'), AES.block_size)))
        self.EncryptSpinner()
        self.Clear()
        return e.decode()
    
    def Decrypt(self, string):
        r = base64.b64decode(string)
        c = AES.new(self.hash_key, AES.MODE_CBC, r[:AES.block_size])
        d = unpad(c.decrypt(r[AES.block_size:]), AES.block_size)
        self.DecryptSpinner()
        self.Clear()
        return d.decode()



