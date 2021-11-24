# caesarplus Decrypt Module
# Owner: awesomelewis2007
# Co-Owner: WolfieBoy

def caesar_decrypt(word,shift):
    c = ''
    for i in word:
        if (i == ' '):
            c += ' '
        else:
            c += (chr(ord(i) - shift))
    return c

