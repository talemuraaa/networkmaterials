import networkx as nx 
import random as rd
import igraph as ig

def closeness_networkx_fast(g: ig.Graph,
                            normalized: bool = True,
                            wf_improved: bool = True) -> list:

    n = g.vcount()
    # Compute connected components
    comp = g.components()
    membership = comp.membership
    sizes = comp.sizes()

    # igraph C implementation: raw closeness = (n-1)/sum_dist
    raw = g.closeness(normalized=True)

    result = [0.0] * n
    for v, rv in enumerate(raw):
        m = sizes[membership[v]]  # size of component containing v
        if rv > 0:
            if normalized:
                if wf_improved:
                    # Scale raw ((n-1)/sumdist) to NetworkX base ((m-1)/sumdist)
                    # and apply WF correction: multiply by (m-1)/(n-1) again
                    scale = ((m-1)/(n-1))**2
                else:
                    # normalized without WF
                    scale = (m-1)/(n-1)
                result[v] = rv * scale
            else:
                # unnormalized: base = m-1 / sumdist = rv * (m-1)/(n-1)
                result[v] = rv * (m-1)/(n-1)
        else:
            result[v] = 0.0
    return result


def random_failure(G:nx.graph):
    
    N=nx.number_of_nodes(G)
    node_list = list(G.nodes)
    rf = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    rd.shuffle(node_list)
    for i in node_list:
        G.remove_node(i)
        maxcom = len(max(nx.connected_components(G), key=len, default=[]))
        rf.append(maxcom / N)

    return rf

def degree_traget_attack(G:nx.graph):

    N=nx.number_of_nodes(G)
    G_ig = ig.Graph.from_networkx(G)
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    dta = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    while(G_ig.vcount() > 0):   
        betweenness=G_ig.degree()
        max_index = betweenness.index(max(betweenness))
        G_ig.delete_vertices(max_index)                
        maxcom=G_ig.components(mode="weak").giant()
        dta.append(maxcom.vcount()/N)
    
    return dta

def closeness_traget_attack(G:nx.graph):
    N=nx.number_of_nodes(G)
    G_ig = ig.Graph.from_networkx(G)
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    cta = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    while(G_ig.vcount() > 0):
        
        closeness=G_ig.harmonic_centrality()
        max_index = closeness.index(max(closeness))
        G_ig.delete_vertices(max_index)      
        maxcom=G_ig.components(mode="weak").giant()
        cta.append(maxcom.vcount()/N)
        
    return cta

def betweenness_target_attack(G:nx.graph):

    N=nx.number_of_nodes(G)
    G_ig = ig.Graph.from_networkx(G)
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    bta = [len(max(nx.connected_components(G), key=len, default=[]))/N]
    while(G_ig.vcount() > 0):
        
        betweenness=G_ig.betweenness()
        max_index = betweenness.index(max(betweenness))
        G_ig.delete_vertices(max_index)                
        maxcom=G_ig.components(mode="weak").giant()
        bta.append(maxcom.vcount()/N)

    return bta
