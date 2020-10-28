#!/usr/bin/env python
import re
import sys

if len(sys.argv) < 3:
    print 'Usage: %s rom.gbc [04 20 xx xx ...]' % __file__
    exit()

f = open(sys.argv[1], 'rb').read()
byte_input = ' '.join(sys.argv[2:]).split()

# convert to regex pattern, replace 'xx' with .
search_term = ''.join([chr(int(x, 16)) if x != 'xx' else '.' for x in byte_input])
x = re.search(search_term, f)

if x is not None:
    print x.group()
    print x.start()
else:
    print 'No match found.'