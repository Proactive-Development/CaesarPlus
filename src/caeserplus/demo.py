import sys
sys.path.append("../../..")
import __init__
__init__.encode("Example")
key,output = __init__.encode("Example")
__init__.decode(key=key,data=output)
