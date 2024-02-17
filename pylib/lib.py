from ctypes import *

# .dylib or .so or .dll
c_lib  = "../clib/lib/libcprogram.dylib"

c_functions = CDLL(c_lib)

assert c_functions.add(10, 20) == (10+20)  

print(c_functions.add(10, 20))