import numpy as np
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from pages.network_models.select_model import model_select

def experiment_hist():
    st.header("次数分布")
    st.write("""
             - 複数のネットワークのヒストグラムを同時に表示します。
             - ネットワークのサイズは各ネットワークで共通です。
             - パラメータをサイドバーで選択し、☑を入れてください。
             - 用意するネットワークの個数と☑の数が同じ場合にのみヒストグラムが表示されます。
             - 次数分布の縦軸の0が合わない気がする。
             """)
    
    network_count = st.slider("用意するネットワークの数",1,10,1,key='n_m')
    network_size = st.slider("各ネットワークのサイズ",10,3000,500,step=10,key='n_s')
    
    networks_list=[]
    max_deg_list=[]
    for i in range(network_count):
        G=model_select(network_size,i)
        networks_list.append(G)
        if G:
            
            degree_sequence=list(nx.degree(G))
            a = max(degree_sequence,key=lambda x:x[1])[1]
            max_deg_list.append(a)
            max_deg=max(max_deg_list)+5
            bins=range(0, max_deg)
    
    gene_hist_button=st.button("次数分布を生成",key='gene_hist',type='primary')
    
    if gene_hist_button :
        fig, ax = plt.subplots(figsize=(7, 6))
        for i in range(network_count):
            G=networks_list[i] 
            degree_sequence=list(G.degree())
            hist,bins=np.histogram(degree_sequence,bins,density=True)
            ax.plot(hist,label=f"network{i}")
            
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        
        ax.set_xlabel('degree')
        ax.grid(True)

        st.pyplot(fig)

    
    
    
    
    
    
