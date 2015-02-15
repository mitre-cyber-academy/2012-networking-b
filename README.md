MITRE STEM CTF

Networking 400 Challenge

Flag: 9D8B1E24

Deliver to contestants:
Just challenge.pcap and possibly the hints mentioned in the explanation.

Files:
	solver.py - used to solve the challenge
	challenge-generator.py - the network daemon used to create the challenge
	127.000.000.001.61416-127.000.000.001.08888 - the contents of the only flow in the pcap
	127.head - the beginning of the flow contents

Mission relationsip: 
We've actually had to do all of this on an adversary protocol. 

Challenge explanation:
challenge.pcap is a packet capture of a file being transferred over the wire (the complete text of Huckleberry Finn from Project Gutenberg) encoded with a 4 byte XOR key (the flag).  In order to solve this, a contestant would need to figure out that they're looking for a multi-byte XOR key (recognizable visually from the patterns in the data) and figure out that they're looking for english ascii text. Either/both of these facts can be given as a hint to reduce the difficulty without making this trivial.

This can be solved using brute force and frequency analysis, but a contestant who realizes that a multibyte XOR can be broken a byte at a time can do it much faster. Because the plaintext is ASCII text, when each byte is correct it decodes to only ASCII text and carriage returns. This can be found visually or programatically.

The solver.py contains the code to attempt a decode a byte at a time, or decode the entire text. 


Example Solution:
use tcpflow to extract the packet contents
> tcpflow -r challenge.pcap

Use head to carve off a bite sized chunk of the file
> head 127.000.000.001.61416-127.000.000.001.08888 > 127.head

Use solver.py to try all possible one byte xor keys on the first, and every subsequent 4th byte.
> python solver.py | less
This could be done in code, but visually you should be able to see the one out of 255 possible keys that results in only ascii text and carriage returns.

In solver.py, comment out the code for first byte, and uncomment the code for second byte.  Repeat for third and fourth bytes. 

Insert the 4 bytes together in the variable KEY in solver ( will be 9d8b1e24 if you've done it right ) comment out the fourth byte code, and uncomment the "print '%s' % multibyte_xor(CYPHERTEXT, KEY)" code.

You should get the first page of Huckleberry Finn.