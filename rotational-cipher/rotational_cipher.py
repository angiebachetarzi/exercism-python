def rotate(text, key):
    def encrypt(letter, key):
        if letter.isalpha():
            if letter.islower():
                base = ord('a')
            else:
                base = ord('A')
            return chr((ord(letter) - base + key)%26 + base)
        else:
            return letter
    return ''.join(map(lambda x: encrypt(x, key), text))
