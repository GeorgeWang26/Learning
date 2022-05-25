import encrypt

def validation():
    print(encrypt.key)
    # encrypt.key += "0"
    print(encrypt.key)

    with open ("encrypted", "r") as f:
        d = encrypt.vigenere_cipher(encrypt.key, f.readline(), "d")
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