#!/usr/bin/env python


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



def multibyte_xor_by_byte(data, key, byte_num):
    output = ""
    key_bytes = len(key) / 2
    for i, char in enumerate(data):
        byte = ord(char)
        key_offset = i % key_bytes * 2
#	print "key_offset = %d, byte = %d" % (key_offset, byte_num)
       	if key_offset == (byte_num * 2):  
		k = key[key_offset:key_offset + 2]
        	#print "k = %s" % k
        	key_byte = int(k, 16)
        	#print "key_byte = %d, byte = %d" % (key_byte, byte)
        	output += chr(byte ^ key_byte)
	else:
		output += " "
    return output


KEY = '9D8B1E24'
FILE = '127.head'

f = open(FILE, 'r')

CYPHERTEXT=f.read()



for i in range(0,255):
	print 'key = %x' % i
	
	# First byte
	TRYKEY = ("%x" % i ) + '000000'	
	print("%s" % multibyte_xor_by_byte(CYPHERTEXT, TRYKEY, 0))
	
	# Second byte
	# TRYKEY = '00' + ("%x" % i ) + '0000'
	# print("%s" % multibyte_xor_by_byte(CYPHERTEXT, TRYKEY, 1))

	# Third byte
	# TRYKEY = '0000' + ("%x" % i ) + '00'
	# print("%s" % multibyte_xor_by_byte(CYPHERTEXT, TRYKEY, 2))

	# Fourth byte
	# TRYKEY = '000000' + ("%x" % i ) 
	# print("%s" % multibyte_xor_by_byte(CYPHERTEXT, TRYKEY, 3))

# Decrypts with the whole key
# print '%s' % multibyte_xor(CYPHERTEXT, KEY)
print "Done"

sys.exit(0)



