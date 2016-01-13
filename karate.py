import networkx as nx
import matplotlib.pyplot as plt

G=nx.karate_club_graph()
print("Node Degree")
for v in G:
    print('%s %s' % (v,G.degree(v)))
print ("\nNumber of edge: ", G.number_of_edges(), "\n")
print ("Edge Betweenness")
betweenness = nx.edge_betweenness_centrality(G)
for key,value in betweenness.items():
    print (key, value)
nx.draw_spring(G)
plt.show()