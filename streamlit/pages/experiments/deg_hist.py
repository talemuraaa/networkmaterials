import numpy as np
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

#ネットワークを受け取り、それぞれ同時にヒストグラムに可視化する。

def Vis_deg_hist(networks_list):
    max_deg_list=[]
    for i in range(len(networks_list)):
        G=networks_list[i]
        degree_sequence=list(nx.degree(G))
        a = max(degree_sequence,key=lambda x:x[1])[1]
        max_deg_list.append(a)
        max_deg=max(max_deg_list)+5
        bins=range(0, max_deg)
    
    gene_hist_button=st.button("次数分布を生成",key='gene_hist',type='primary')
    
    if gene_hist_button :
        for i in range(networks_list):
            G=networks_list[i]
            degree_sequence=list(G.degree())
            hist,bins=np.histogram(degree_sequence,bins,density=True)
            plt.plot(hist,label=f"network{i}")
            
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        
        plt.xlabel('degree')
        plt.grid(True)
        plt.ylim(bottom=0)
        
        return st.pyplot(plt)