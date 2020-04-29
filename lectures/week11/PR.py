import networkx as nx
from operator import itemgetter

G=nx.DiGraph()

f=open('flow.txt')
for line in f:
	source,target,w=line.strip().split('\t')
	w=int(w)
	G.add_edge(source,target,weight=w)
f.close()

pr = nx.pagerank(G, alpha=0.9,weight='weight')


fw=open('ranking.txt','w')
srt=sorted(pr.items(),key=itemgetter(1),reverse=True)
for x,y in srt:
	fw.write(x+'\t'+str(y)+'\n')
fw.close()


