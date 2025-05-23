import streamlit as st
import networkx as nx 
import random as rd
import igraph as ig


def attack_betweenness(G_ig):
    bta = [1]
    N=G_ig.vcount()
    while(G_ig.vcount() > 0):
        
        betweenness=G_ig.betweenness()
        max_index = betweenness.index(max(betweenness))
        G_ig.delete_vertices(max_index)                
        maxcom=G_ig.components(mode="weak").giant()
        bta.append(maxcom.vcount()/N)
      
    return bta


#igraphを用いたランダム障害

    if strategy == "ランダム障害":
        K=list(range(N))
        
        if st.button("実行",key='strategy_button'):
            node_names = G_ig.vs["name"].copy()
            rd.shuffle(node_names)
            rf =[1]
            i=0
            idx=0
            for i in node_names:
                G_ig.delete_vertices(i)
                maxcom=G_ig.components(mode="weak").giant()
                rf.append(maxcom.vcount()/N)
                idx = idx+1
                progress_bar.progress((idx/N))
            
            st.write(len(rf))
            progress_placeholder.empty()    
            return rf