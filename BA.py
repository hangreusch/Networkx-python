'''
Created on Apr 14, 2015

@author: hang
'''

import networkx as nx
import matplotlib.pyplot as plt

for N in [1000,2000,5000]: #for loop to draw 3 graphs with number of nodes is 1000, 2000, 5000
    G=nx.barabasi_albert_graph(N,1) #method to draw graph using barabasi-albert algorithm
    nx.draw_circular(G) #draw graph
    plt.show() #show graph
    