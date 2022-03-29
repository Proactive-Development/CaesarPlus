import pytest
import sys
import os

from caesarplus import encode
from caesarplus import decode

def test_encrypt():
    encode("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
def test_decrypt():
    key,output = encode("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    decode(key=key,data=output)