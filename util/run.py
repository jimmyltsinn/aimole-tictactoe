#!/usr/local/python

import sys

if len(sys.argv) < 3: 
    print 'Usage: %s verdict p1.o p2.o ...'%(sys.argv[0])
    sys.exit(-1)

print sys.argv

verdictPath = sys.argv[1]
playerList = sys.argv[2:]

print 'Verdict: %s' % verdictPath
print 'Number of player: %d' % len(playerList)
print 'Players: %s' % str(playerList)

## TODO
