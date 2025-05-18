import streamlit as st
import networkx as nx 
import random as rd
import igraph as ig

#ver.2

def ig_select_strategy(G):
    G_ig = ig.Graph.from_networkx(G)
    N=G_ig.vcount()
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    
    strategy=st.selectbox("攻撃戦略",
                          ("ランダム障害","標的型攻撃(degree)","標的型攻撃(closeness)","標的型攻撃(betweenness)"),
                          key='strategy')
    
    
    progress_placeholder = st.empty()
    progress_bar = progress_placeholder.progress(0)
    
    if strategy == "ランダム障害":
            N=nx.number_of_nodes(G)
            K=list(range(N))
            
            if st.button("実行",key='strategy_button'):
                sampl = rd.sample(K,N)
                rf =[1]
                i=0
                idx=0
                for i in sampl:
                    G.remove_node(i)
                    maxcom=len(max(nx.connected_components(G),key=len,default=[0]))
                    rf.append(maxcom/N)
                    idx = idx+1
                    progress_bar.progress((idx/N))
                
                st.write(len(rf))
                progress_placeholder.empty()    
                return rf
    
    if strategy == "標的型攻撃(degree)":
        if st.button("実行",key='strategy_button'):
            dta = [1]
            idx=0
            while(G_ig.vcount() > 0):   
                betweenness=G_ig.degree()
                max_index = betweenness.index(max(betweenness))
                G_ig.delete_vertices(max_index)                
                maxcom=G_ig.components(mode="weak").giant()
                dta.append(maxcom.vcount()/N)
  
                idx = idx+1
                progress_bar.progress((idx/N))
                
            progress_placeholder.empty()            
            return dta    
    
    if strategy == "標的型攻撃(closeness)":
        if st.button("実行",key='strategy_button'):
            cta = [1]
            idx=0
            while(G_ig.vcount() > 0):
                
                betweenness=G_ig.closeness()
                max_index = betweenness.index(max(betweenness))
                G_ig.delete_vertices(max_index)                
                maxcom=G_ig.components(mode="weak").giant()
                cta.append(maxcom.vcount()/N)
  
                idx = idx+1
                progress_bar.progress((idx/N))
                
            progress_placeholder.empty()            
            return cta                       
                        
    if strategy == "標的型攻撃(betweenness)":
        if st.button("実行",key='strategy_button'):
            bta = [1]
            idx=0
            while(G_ig.vcount() > 0):
                
                betweenness=G_ig.betweenness()
                max_index = betweenness.index(max(betweenness))
                G_ig.delete_vertices(max_index)                
                maxcom=G_ig.components(mode="weak").giant()
                bta.append(maxcom.vcount()/N)
  
                idx = idx+1
                progress_bar.progress((idx/N))
                
            progress_placeholder.empty()            
            return bta
    
#ver.1
    
def select_strategy(G):

    strategy=st.selectbox("攻撃戦略",
                          ("ランダム障害","標的型攻撃(degree)","標的型攻撃(closeness)","標的型攻撃(betweenness)"),
                          key='strategy')
    N=nx.number_of_nodes(G)
    
    progress_placeholder = st.empty()
    progress_bar = progress_placeholder.progress(0)
      
    if strategy == "ランダム障害":
        N=nx.number_of_nodes(G)
        K=list(range(N))
        
        if st.button("実行",key='strategy_button'):
            sampl = rd.sample(K,N)
            rf =[1]
            i=0
            idx=0
            for i in sampl:
                G.remove_node(i)
                maxcom=len(max(nx.connected_components(G),key=len,default=[0]))
                rf.append(maxcom/N)
                idx = idx+1
                progress_bar.progress((idx/N))
            
            st.write(len(rf))
            progress_placeholder.empty()    
            return rf
    
    if strategy == "標的型攻撃(degree)":
        if st.button("実行",key='strategy_button'):
            dta =[1]
            idx=0
            while(nx.number_of_nodes(G) > 0):
                
                d=dict(nx.degree_centrality(G))
                G.remove_node(max(d,key=d.get))                
                maxcom2=len(max(nx.connected_components(G),key=len,default=[0]))
                dta.append(maxcom2/N)
                
                idx = idx+1
                progress_bar.progress((idx/N))
                
            progress_placeholder.empty()                
            return dta
               
    if strategy == "標的型攻撃(closeness)":
        if st.button("実行",key='strategy_button'):
            cta = [1]
            idx=0
            while(nx.number_of_nodes(G) > 0):
                d=dict(nx.closeness_centrality(G))
                G.remove_node(max(d,key=d.get))                
                maxcom2=len(max(nx.connected_components(G),key=len,default=[0]))
                cta.append(maxcom2/N)
                idx = idx+1
                progress_bar.progress((idx/N))
                
            progress_placeholder.empty()                
            return cta
                       
    if strategy == "標的型攻撃(betweenness)":
        if st.button("実行",key='strategy_button'):
            bta = [1]
            idx=0
            while(nx.number_of_nodes(G) > 0):
                
                d=dict(nx.betweenness_centrality(G))
                G.remove_node(max(d,key=d.get))                
                maxcom2=len(max(nx.connected_components(G),key=len,default=[0]))
                bta.append(maxcom2/N)
  
                idx = idx+1
                progress_bar.progress((idx/N))
                
            progress_placeholder.empty()            
            return bta
  
    