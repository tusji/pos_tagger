lowprob = 1e-12
# Helps visualize the steps of Viterbi.
def print_dptable(V):
	print ("	")
	for i in range(len(V)): 
		print("%7d" % i)

	for y in V[0].keys():
		print ("%.5s: " % y)
		for t in range(len(V)):
			print ("%.7s" % ("%f" % V[t][y]))

def viterbi(obs, states, start_p, trans_p, emit_p):
	V = [{}]
	path = {}

	# Initialize base cases (t == 0)
	for y in states:
		if not start_p.__contains__(y):
			start_p.update({y:lowprob})
		if not emit_p.__contains__((obs[0],y)):
			emit_p.update({(obs[0],y):lowprob})
		V[0][y] = start_p[y] * emit_p[(obs[0],y)]
		path[y] = [y]


	# Run Viterbi for t > 0
	for t in range(1,len(obs)):
		V.append({})
		newpath = {}

		for y in states:
			if not emit_p.__contains__((obs[t],y)):
				emit_p.update({(obs[t],y):lowprob})
			(prob, state) = max([(V[t-1][y0] * trans_p[(y0,y)] * emit_p[(obs[t],y)], y0) for y0 in states])
			V[t][y] = prob
			newpath[y] = path[state] + [y]

		# Don't need to remember the old paths
		path = newpath

	#print_dptable(V)
	(prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
	#print((prob, path[state]))
	return (prob, path[state])