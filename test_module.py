# caesarplus Main Module
# Owner: awesomelewis2007
# Co-Owner: WolfieBoy
import pytest
import sys
import os

from src.caesarplus import encode
from src.caesarplus import decode

def test_encrypt():
    encode("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
def test_decrypt():
    key,output = encode("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    decode(key=key,data=output)