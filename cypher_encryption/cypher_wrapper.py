import cypher

def validation():
    # encrypt.vigenere_cipher()
    key = cypher.get_key()
    # key += "0"
    print(key)
    f = open("encrypted", "r")
    d = cypher.vigenere_cipher(key, f.read(), "d")
    print(d == cypher.plain_text)
    if d == cypher.plain_text:
        print("proceed")
    else:
        print("quit now")
        quit()
        print("should never be printed")

    print("only here if true")

if __name__ == "__main__":
    validation()