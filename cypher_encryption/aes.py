# use AES GCM-256 for encryption
# https://nitratine.net/blog/post/python-gcm-encryption-tutorial/

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from getmac import get_mac_address as gma
import subprocess


data = "WHJLQJH:OIE@*(#_!*$!@U$B!@Y$_(*!@&JHJ#K!B#I!@*)(#"
file_location = "/home/ubuntu/Desktop/data.encrypted"

def get_password():
    s = subprocess.Popen("sudo dmidecode -t system | grep UUID", shell=True, stdout=subprocess.PIPE).stdout.read()
    s = s.decode()[7:-1]
    pwd = gma() + s
    print("password:", pwd)
    return pwd

def encrypt():
    salt = get_random_bytes(32)
    key = scrypt(get_password(), salt, key_len=32, N=2**20, r=8, p=1)  # work facrtor N can be from 2^14 to 2^20, change based on time cost
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    print("ciphertext len:", len(ciphertext))
    with open(file_location, "wb") as f:
        f.writelines([salt, cipher.nonce, ciphertext, tag])
        f.close()

def decrypt():
    f = open(file_location, "rb")
    text = f.read()
    salt = text[:32]
    # fake_key = get_password() + "**********"
    # key = scrypt(fake_key, salt, key_len=32, N=2**20, r=8, p=1)
    key = scrypt(get_password(), salt, key_len=32, N=2**20, r=8, p=1)
    nonce = text[32:48]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext = text[48:-16]
    try:
        msg = cipher.decrypt(ciphertext).decode()
    except UnicodeDecodeError as e:
        print("\n\n==============================\ninvalid credential\n==============================\n\n")
        quit()
    tag = text[-16:]
    try:
        cipher.verify(tag)
    except ValueError as e:
        f.close()
        print("\n\n==============================\ntag verification failed\n==============================\n\n")
        quit()
    f.close()
    return msg

def verify():
    msg = decrypt()
    if msg != data:
        print("verification failed, exit now")
        quit()
    print("verification success\n-------------------------------------------------------\n")

if __name__ == "__main__":
    encrypt()
    verify()