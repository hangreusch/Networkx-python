'''
Created on Apr 15, 2015

@author: hang
'''
import networkx as nx
import math
import matplotlib.pyplot as plt

for N in [1000,2000,5000]:
    print ("For graph having ", N, " nodes:")
    G=nx.barabasi_albert_graph(N, 1)
    dictionary=nx.degree(G) #degree of each single node          
    list1= [] 
    for hang, value in dictionary.items():
        list1.insert(hang, value) #store degree of each node in the list1
    print("Degree k: ", list1) 
    
    list2 = [] 
    for hang, value in dictionary.items():
        list2.insert(hang, math.log10(value)) #store log (degree) in the list2
    print("Log (k): ", list2)
    
    list3 = [] 
    i = 0
    while i < N:
        list3.insert(i, math.log10(list1.count(list1[i]))) #store log N(degree) in the list
        i += 1
    print("Log N(k): ", list3) 
    
    plt.title("Degree Distribution")
    plt.ylabel("Log N(k)")
    plt.xlabel("Log (k)")
    plt.plot(list2,list3,'ro')
    plt.axis([0,4,0,4])
    plt.show()