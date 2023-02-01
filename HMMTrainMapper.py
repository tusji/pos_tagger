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



for lines in sys.stdin:
    dic = json.loads(lines)
    for j in dic:
        #build p2p
        for k in range((len(j['title_pos'])-1)):
            if k == 0:
                initwnum += 1
                if initw.__contains__(j['title_pos'][k]):
                    initw[j['title_pos'][0]] += 1
                else :
                    initw.update({j['title_pos'][0] : 1})
            if j['title_pos'][k] not in tag:
                tag.append(j['title_pos'][k])
            if p2pnum.__contains__(j['title_pos'][k]):
                p2pnum[j['title_pos'][k]] += 1
            else:
                p2pnum.update({j['title_pos'][k] : 1})
            if p2p.__contains__((j['title_pos'][k],j['title_pos'][k+1])):
                p2p[(j['title_pos'][k],j['title_pos'][k+1])]+=1
            else :
                p2p.update({(j['title_pos'][k],j['title_pos'][k+1]) : 1})
        for k in range((len(j['context_pos'])-1)):
            if k == 0:
                initwnum += 1
                if initw.__contains__(j['context_pos'][k]):
                    initw[j['context_pos'][0]] += 1
                else :
                    initw.update({j['context_pos'][0] : 1})
            if j['context_pos'][k] not in tag:
                tag.append(j['context_pos'][k])
            if p2pnum.__contains__(j['context_pos'][k]):
                p2pnum[j['context_pos'][k]] += 1
            else:
                p2pnum.update({j['context_pos'][k] : 1})
            if p2p.__contains__((j['context_pos'][k],j['context_pos'][k+1])):
                p2p[(j['context_pos'][k],j['context_pos'][k+1])]+=1
            else :
                p2p.update({(j['context_pos'][k],j['context_pos'][k+1]) : 1})
        #build p2w and initialW
        #part of title
        for k in range(len(j['title_w'])):
            if p2wnum.__contains__(j['title_pos'][k]):
                p2wnum[j['title_pos'][k]] += 1
            else:
                p2wnum.update({j['title_pos'][k] : 1})					
            if p2w.__contains__((j['title_w'][k],j['title_pos'][k])):
                p2w[(j['title_w'][k],j['title_pos'][k])] += 1 
            else :
                p2w.update({(j['title_w'][k],j['title_pos'][k]) : 1})  
            #part of context
        for k in range(len(j['context_w'])):
            if p2wnum.__contains__(j['context_pos'][k]):
                p2wnum[j['context_pos'][k]] += 1
            else:
                p2wnum.update({j['context_pos'][k] : 1})
            if p2w.__contains__((j['context_w'][k],j['context_pos'][k])):
                p2w[(j['context_w'][k],j['context_pos'][k])] += 1 
            else :
                p2w.update({(j['context_w'][k],j['context_pos'][k]) : 1})

resultdict = {"p2p":p2p, "p2pnum":p2pnum, "p2w":p2w, "p2wnum":p2wnum, "initw":initw, "initwnum":initwnum, "tag":tag}
print(pickle.dumps(resultdictprotocol = pickle.HIGHEST_PROTOCOL))		

