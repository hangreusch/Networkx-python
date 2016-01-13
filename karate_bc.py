'''
Created on Apr 20, 2015

@author: hang
'''
import networkx as nx
import matplotlib.pyplot as plt
from betweenness import betweenness

G=nx.karate_club_graph()

print ("Initially")
print("Number of edges = ",G.number_of_edges()) 

#Girvan-Newman method to partition graph
def GirvanNewman(G):
    no_component = nx.number_connected_components(G) #number of components 
    print("Number of components: ", no_component)
    number_comp = no_component
    while number_comp <= no_component: #while loop to partition graph into separate components 
        betweenness = nx.edge_betweenness_centrality(G)   #edge betweenness 
        highest = max(betweenness.values()) #highest betweenness
        print("Highest betweenness: ", highest)
        for key, value in betweenness.items():
            if float(value) == highest:
                print("Edge removed ", key[0],key[1])
                G.remove_edge(key[0],key[1])    #remove the edge with highest betweenness
                nx.draw_spectral(G) #draw graph after edge removed
                plt.show()
        number_comp = nx.number_connected_components(G)   #recalculate number of components                                         
        print("\nNumber of components: ", number_comp)    #print number of components

GirvanNewman(G)
print ("Partition finishes")
print("Number of edges = ", G.number_of_edges()) #print number of edges after graph is partitioned
nx.draw_spectral(G) #draw graph after finishing partition process
plt.show()
