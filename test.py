#!/usr/bin/env python


import socket
import sys


def multibyte_xor(data, key):
    output = ""
    key_bytes = len(key) / 2
    for i, char in enumerate(data):
        byte = ord(char)
        key_offset = i % key_bytes * 2
        k = key[key_offset:key_offset + 2]
        #print "k = %s" % k
        key_byte = int(k, 16)
        #print "key_byte = %d, byte = %d" % (key_byte, byte)
        output += chr(byte ^ key_byte)
    return output


HOST = 'localhost'
PORT = 8888
KEY = '9D8B1E24'
FILE = '/Users/adamp/pg76.txt'

try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(1)

try:
  sock.connect((HOST, PORT))
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(2)

f = open(FILE, 'r')

SENDTEXT=f.read()




sock.send("%s" % (multibyte_xor(SENDTEXT, KEY)))

sock.close()

print "Done"

sys.exit(0)



