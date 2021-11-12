def caesar_encrypt(word,shift):
    c = ''
    for i in word:
        if (i == ' '):
            c += ' '
        else:
            c += (chr(ord(i) + shift))
    return c
