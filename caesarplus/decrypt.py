def caesar_decrypt(word,shift):
    caesar = ''
    for i in word:
        if (i == ' '):
            caesar += ' '
        else:
            caesar += (chr(ord(i) - shift))
    return caesar

