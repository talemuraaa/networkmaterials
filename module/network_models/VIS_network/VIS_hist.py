import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#受け取ったネットワークのヒストグラムを表示する。

def visualization_hist(G):
    fig, ax = plt.subplots(figsize=(7, 4))
    degree_sequence=list(nx.degree(G))
    max_deg = max(degree_sequence,key=lambda x:x[1])[1]
    bins=range(0, max_deg+5)
    
    hist,bins=np.histogram(degree_sequence,bins)
    ax.plot(hist)
    ax.set_xlabel('degree')
    ax.grid(True)
    fig.tight_layout()
    ax.set_ylim(bottom=0)
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