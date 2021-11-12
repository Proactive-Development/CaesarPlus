# Caeserplus Main Module
# Owner: awesomelewis2007
# Co-Owner: WolfieBoy
import pytest
import sys
import os
#This code here is to import caeserplus.py
os.chdir("tests")
sys.path.append("..")
import caeserplus
def test_encrypt():
    caeserplus.encode("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
def test_decrypt():
    key,output = caeserplus.encode("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    caeserplus.decode(key=key,data=output)