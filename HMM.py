import pickle
from ckiptagger import WS
import Viterbi as vi

ws = WS("./data")

resultpos = []
with open("part-00000","rb") as f:
	matrix = pickle.load(f)
states = matrix['tag']
start_p = matrix['initw']
trans_p = matrix['p2p']
emit_p = matrix['p2w']
for y in states:
	for y0 in states:
		if not trans_p.__contains__((y0,y)):
			trans_p.update({(y0,y):1e-12})
print("please input chinese sentence...>")
while True:
	ckipResult  = ws([input()])
	obs = ckipResult[0]
	result = vi.viterbi(obs, states, start_p, trans_p, emit_p)
	print("My model result:\n",result[1])
	