import numpy as np
import pandas as pd
import streamlit as st
import networkx as nx

def compute_heterogeneity(G: nx.Graph) -> float:
    """
    Compute the network heterogeneity defined as
    \[ H = \frac{\langle k^2 \rangle}{\langle k \rangle^2 } \],
    where k is the node degree.

    Parameters
    ----------
    G : nx.Graph
        Input graph.

    Returns
    -------
    float
        Heterogeneity measure. Returns NaN if undefined.
    """
    n = G.number_of_nodes()
    if n == 0:
        return float('nan')

    degrees = np.array([deg for _, deg in G.degree()], dtype=float)
    mean_deg = degrees.mean()
    if mean_deg == 0:
        return float('nan')

    mean_sq = np.mean(degrees ** 2)
    return mean_sq / (mean_deg ** 2)

def heterogeneity(G:nx.Graph):
    d=list(dict(nx.degree(G)).values())
    k1=sum(np.square(d))/G.number_of_nodes()
    k2=(np.mean(d))**2
    k3=k1/k2
    return k3

def weighted_average_shortest_path(G)-> float:
    if nx.is_connected(G):
        return nx.average_shortest_path_length(G)   
    avg_lengths = []
    weights = []   
    for component in nx.connected_components(G):
        subgraph = G.subgraph(component)
        n = len(subgraph)
        if n <= 1:
            continue
        avg_len = nx.average_shortest_path_length(subgraph)
        weight = n * (n - 1) / 2 
        avg_lengths.append(avg_len)
        weights.append(weight)
    if not weights:
        return float("inf")
    
    return np.average(avg_lengths, weights=weights)
    
def net_parameter(G: nx.Graph,use_streamlit: bool = True,caption: str = "Network Parameters"):
    
    metrics = {
        'ノード数': G.number_of_nodes(),
        'リンク数': G.number_of_edges(),
        '連結成分': nx.number_connected_components(G),
        'リンク密度': nx.density(G),
        '平均最短経路長': weighted_average_shortest_path(G),
        'クラスター係数': nx.average_clustering(G),
        '不均一性': compute_heterogeneity(G),
    }
    
    df = pd.DataFrame.from_dict(
            {caption: metrics}, orient='index'
        ).T  # Transpose to show metrics as rows
    
    if use_streamlit:
        st.write(f"### {caption}")
        st.dataframe(df, width=650)


    return df
    
