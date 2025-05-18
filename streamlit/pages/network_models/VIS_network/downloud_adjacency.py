import pandas as pd
import streamlit as st
import networkx as nx
from io import StringIO

def downloud_adjacency_list_button(G):
    adj_dict={node: list(G.neighbors(node)) for node in G.nodes()}
            
    df = pd.DataFrame([
        {'Node': node, 'Neighbors': ','.join(map(str, neighbors))}
        for node, neighbors in adj_dict.items()
    ])
    
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
    
    

#adj_list=nx.to_pandas_edgelist(G)

#adj_list={node: list(G.adj[node])for node in G.nodes}
#df = pd.DataFrame([(k, v) for k, vs in adj_list.items() for v in vs])