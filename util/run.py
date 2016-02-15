#!/usr/local/python

import sys
import os
import subprocess
import json
import io

if len(sys.argv) < 3:
    print 'Usage: %s verdict execP1 execP2 ...' % sys.argv[0]
    sys.exit(-1)

print sys.argv

verdictPath = sys.argv[1]
playerPath = sys.argv[2:]
playerNumber = len(playerPath)

print 'Verdict: %s' % verdictPath
print 'Number of player: %d' % playerNumber
print 'Players: %s' % str(playerPath)

verdict = subprocess.Popen(['python', '-u', os.path.abspath(verdictPath)],
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE)
players = []
for i in xrange(0, playerNumber):
    players.append(subprocess.Popen(os.path.abspath(playerPath[i]),
                   stdin=subprocess.PIPE, stdout=subprocess.PIPE))

verdict.stdin.write(json.dumps({'command': 'start'}) + '\n')
verdict.stdin.flush()

while True:
    verdictData = json.loads(verdict.stdout.readline())
    # All stderr ignored
    # verdictErr = verdict.stderr.readline()
    print verdictData

    if verdictData['action'] == 'next':
        nextPlayer = players[verdictData['nextPlayer']]
        nextPlayer.stdin.write(verdictData['writeMsg'])
        playerData = nextPlayer.stdout.readline()

        playerMsg = {}
        playerMsg['player'] = verdictData['nextPlayer']
        playerMsg['command'] = 'player'
        playerMsg['time'] = 0
        playerMsg['stdout'] = playerData
        verdict.stdin.write(json.dumps(playerMsg) + '\n')
    elif verdictData['action'] == 'stop':
        print "Verdict: Stop"
        break
    elif verdictData['action'] == 'error':
        print "Verdict: Error (%s) " % verdictData['errorMessage']
        break

(out, err) = verdict.communicate()
if out != None and out != "": 
    print "Verdict stdout: %s" % out
if err != None and err != "":
    print "Verdict stderr: %s" % err

for i in xrange(0, playerNumber): 
    players[i].kill()
    (out, err) = players[i].communicate()
    if out != None and out != "": 
        print "P%d stdout: %s" % (i, out)
    if err != None and err != "":  
        print "P%d stderr: %s" % (i, err)
