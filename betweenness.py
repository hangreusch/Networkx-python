'''
Created on Apr 17, 2015

@author: hang
'''
import networkx as nx

G=nx.karate_club_graph()
betweenness = nx.edge_betweenness_centrality(G) #edge betweenness
print ("List of edges and their corresponding betweenness:")
print (betweenness,"\n")
betweenness_sort = sorted(betweenness.values()) #sort betweenness
betweenness_sort.reverse() #arrange betweenness in descending order
print("Sorted betweenness:")
print (betweenness_sort,"\n")
for key,value in betweenness.items():
    if value == betweenness_sort[0]: #highest betweenness
        print("Edge: ",key, "has highest betweenness which is ", value)