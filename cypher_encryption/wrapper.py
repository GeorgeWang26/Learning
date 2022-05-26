import encrypt

def validation():
    # encrypt.vigenere_cipher()
    key = encrypt.get_key()
    # key += "0"
    print(key)
    f = open("encrypted", "r")
    d = encrypt.vigenere_cipher(key, f.read(), "d")
    print(d == encrypt.plain_text)
    if d == encrypt.plain_text:
        print("proceed")
    else:
        print("quit now")
        quit()
        print("should never be printed")

    print("only here if true")

if __name__ == "__main__":
    validation()