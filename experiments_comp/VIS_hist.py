import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#受け取ったネットワークのヒストグラムを表示する。

def visualization_hist(G:nx.graph):
    fig, ax = plt.subplots(figsize=(7, 4))
    degrees = [degree for _, degree in G.degree()]
    
    max_deg = max(degrees)
    bins=range(0, max_deg+5)
    
    hist, bins = np.histogram(degrees, bins=bins)
    #x = bin_edges[:-1]
    
    ax.plot(hist)
    
    #ax.bar(x, hist, width=0.8, edgecolor='black', align='center')

    ax.set_xlabel("Degree")
    ax.set_ylabel("Frequency")
    ax.grid(linestyle='--', alpha=0.7)


    fig.tight_layout()
    st.pyplot(fig)
    

#複数のネットワークをリストで一度に受け取り、同時に一枚にヒストグラムを表示する。
def multi_visualization_hist(networks_list):
    max_deg_list=[]
    fig, ax = plt.subplots(figsize=(7, 4))
    for i in range(len(networks_list)):
        G=networks_list[i]
        
        degree_sequence=list(nx.degree(G))
        a = max(degree_sequence,key=lambda x:x[1])[1]
        max_deg_list.append(a)
        max_deg=max(max_deg_list)+5
            
    bins=range(0, max_deg)
      
    for i in range(networks_list):
        G=networks_list[i]
        degree_sequence=list(G.degree())
        hist,bins=np.histogram(degree_sequence,bins,density=True)
        ax.plot(hist,label=f"network{i}")
            
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    ax.xlabel('degree')
    ax.grid(True)
    
    return st.pyplot(fig)