import networkx as nx
import numpy as np

def Molly_Reed(G:nx.Graph)-> float:
    N=G.number_of_nodes()
    d=list(dict(nx.degree(G)).values())
    square_dgeree_average = sum(np.square(d))/N
    degree_average = sum(d)/N
    
    return square_dgeree_average/degree_average
    
def Molly_Reed_criterion(G:nx.graph)-> bool:
    if Molly_Reed(G) > 2:
        return True
    else:
        return False
    
def robustness(LCC:list)->float:
    return sum(LCC)/len(LCC)