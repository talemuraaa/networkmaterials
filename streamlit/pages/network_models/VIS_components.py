import numpy as np
import pandas as pd
import streamlit as st
import networkx as nx
from io import StringIO
from pages.network_models import VIS_components

def heterogeneity(G): 
    d=list(dict(nx.degree(G)).values())
    k1=sum(np.square(d))/G.number_of_nodes()
    k2=(np.mean(d))**2
    k3=k1/k2
    return k3

def weighted_average_shortest_path(G):
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
    
def net_parameter(G):
    
    number_of_nodes=nx.number_of_nodes(G)
    number_of_edges=nx.number_of_edges(G)
    number_of_components=nx.number_connected_components(G)
    density=nx.density(G)
    average_clustering=nx.average_clustering(G)
    heterogeneity=VIS_components.heterogeneity(G)
    average_shortest_path_length=VIS_components.weighted_average_shortest_path(G)
    
    df=pd.DataFrame(
        {"":[number_of_nodes,number_of_edges,number_of_components,density,average_shortest_path_length,average_clustering,heterogeneity] },
         index=['ノード数','リンク数','連結成分','リンク密度','平均最短経路長','クラスター係数','不均一性']
        )
    
    st.dataframe(df,width=650)

def downloud_adjacency_list_button(G):
    adj_list={node: list(G.adj[node])for node in G.nodes}
    df = pd.DataFrame([(k, v) for k, vs in adj_list.items() for v in vs])
    
    csv_buffer = StringIO()
    df.to_csv(csv_buffer,index=False)
    csv_data=csv_buffer.getvalue()
    
    st.download_button(
        label="download",
        data=csv_data,        
        file_name="adj_list.csv",
        mime="text/csv",
        type='primary'
        )   