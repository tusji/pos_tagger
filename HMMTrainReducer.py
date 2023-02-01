#!/usr/bin/env python
import __future__
import sys
import json
import pickle
p2p = {}
p2pnum = {}
p2w = {}
p2wnum = {}
initw = {}
initwnum = 0
tag = []

#process and combine input 
for line in sys.stdin:
    inputline = pickle.loads(line)
    initwnum += inputline["initwnum"]
    for i in inputline["p2p"].key:
        if p2p.__contains__(i):
            p2p[i]+=inputline["p2p"][i]
        else:
            p2pnum.update(p2p[i])
    for i in inputline["p2w"].key:
        if p2w.__contains__(i):
            p2w[i]+=inputline["p2w"][i]
        else:
            p2wnum.update(p2w[i])
    for i in inputline["p2pnum"].key:
        if p2pnum.__contains__(i):
            p2pnum[i]+=inputline["p2pnum"][i]
        else:
            p2pnum.update(p2pnum[i])
    for i in inputline["p2wnum"].key:
        if p2wnum.__contains__(i):
            p2wnum[i]+=inputline["p2wnum"][i]
        else:
            p2wnum.update(p2wnum[i])
    for i in inputline["initw"].key:
        if initw.__contains__(i):
            initw[i]+=inputline["initw"][i]
        else:
            initw.update(initw[i])
    for i in inputline["tag"]:
        if i not in tag:
            tag.append(i)
   


#compute rate of each matrix
for i in p2pnum.keys():
	for j in p2p.keys():
		if i == j[0]:
			p2p[j] /= p2pnum[i]
for i in initw.keys():
	initw[i] /= initwnum
	
for i in p2wnum.keys():
	for j in p2w.keys():
		if i == j[1]:
			p2w[j] /= p2wnum[i]

#output matrix to file
resultdic = {"p2p":p2p, "p2w":p2w, "initw":initw, "tag":tag }

print(pickle.dumps(resultdic, protocol = pickle.HIGHEST_PROTOCOL))
