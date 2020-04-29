import re
from nltk.corpus import stopwords
import networkx as nx
from nltk.tokenize import sent_tokenize
from networkx.algorithms import community

sw=set(stopwords.words('english'))

G=nx.Graph()

c=0
f=open('article.txt')
text=f.read()
f.close()

#split sentences
sentences=sent_tokenize(text)
for sentence in sentences:
    sentence=re.sub('[^a-z]',' ',sentence.lower()).strip() # clean the sentence
    terms=sentence.split()
        
    for i in range(len(terms)): # for each term
        if terms[i] in sw or len(terms[i])<3:continue # ignore stopwords and small terms

        for j in range(i+1,len(terms)):
            if terms[j] in sw or len(terms[j])<3:continue# ignore stopwords and small terms
                    
            if not G.has_edge(terms[i],terms[j]):  # add edge if it is not there already

                G.add_edge(terms[i],terms[j]) 
                G[terms[i]][terms[j]]['freq']=1 # the count is 1
                    
                      
            else:
                G[terms[i]][terms[j]]['freq']+=1 # existing edge, increment the count
            
            
f.close()


#remove all edges with a freq less than 3
remove = []
for N1,N2 in G.edges(): # for each edge
    if G[N1][N2]['freq']<3:remove.append((N1,N2)) # add it to the 'remove' list

G.remove_edges_from(remove) # filter

#find all maximal cliques   
cliques=list(nx.find_cliques(G))
sorted_cliques= sorted(cliques, key=len,reverse=True) # sort cliques by size
print (sorted_cliques[0])

#find all k-cliques communities   
kcliques=list(community.k_clique_communities(G,3))
sorted_cliques= sorted(kcliques, key=len,reverse=True) # sort cliques by size
print (sorted_cliques[0])







