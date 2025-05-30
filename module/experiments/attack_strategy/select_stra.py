import streamlit as st
import networkx as nx 
import random as rd
import igraph as ig

#近接中心性を計算
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

#プログレスバーを追加。ver.5

def select_strategys_prog(G,strategy_list,progress_callback=None):

    N=G.number_of_nodes()
    result={}
    total_steps = len(strategy_list)
    

    
    for idx,strategy in enumerate(strategy_list):
        if progress_callback:
            progress_callback(int(idx / total_steps * 100))
        G_copy = G.copy()
        G_ig = ig.Graph.from_networkx(G)    
        G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]      
          

        if strategy == "ランダム障害":
            rf = [1]
            node_list = list(G_copy.nodes)
            rd.shuffle(node_list)
            for i in node_list:
                G_copy.remove_node(i)
                maxcom = len(max(nx.connected_components(G_copy), key=len, default=[]))
                rf.append(maxcom / N)
                
            result["random failure"]=rf
        
        elif strategy == "標的型攻撃(degree)":
            dta = [1]
            while(G_ig.vcount() > 0):   
                betweenness=G_ig.degree()
                max_index = betweenness.index(max(betweenness))
                G_ig.delete_vertices(max_index)                
                maxcom=G_ig.components(mode="weak").giant()
                dta.append(maxcom.vcount()/N)
            
            result["degree"] =dta
        
        elif strategy == "標的型攻撃(closeness)":
            cta = [1]
            while(G_ig.vcount() > 0):
                
                closeness=closeness_networkx_fast(G_ig)
                max_index = closeness.index(max(closeness))
                G_ig.delete_vertices(max_index)      
                maxcom=G_ig.components(mode="weak").giant()
                cta.append(maxcom.vcount()/N)
                
            result["closeness"]=cta
        
        elif strategy == "標的型攻撃(betweenness)":
            bta = [1]
            while(G_ig.vcount() > 0):
                
                betweenness=G_ig.betweenness()
                max_index = betweenness.index(max(betweenness))
                G_ig.delete_vertices(max_index)                
                maxcom=G_ig.components(mode="weak").giant()
                bta.append(maxcom.vcount()/N)
     
            result["betweenness"]=bta
    
    if progress_callback:
        progress_callback(100)  # 完了
    
    return result
#multiselect対応ver.4

def ig_select_strategys(G,strategy_list):

    N=G.number_of_nodes()

    
    result={}
    
    for strategy in strategy_list:
        G_copy = G.copy()
        G_ig = ig.Graph.from_networkx(G)    
        G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]        

        if strategy == "ランダム障害":
            rf = [1]
            node_list = list(G_copy.nodes)
            rd.shuffle(node_list)
            for i in node_list:
                G_copy.remove_node(i)
                maxcom = len(max(nx.connected_components(G_copy), key=len, default=[]))
                rf.append(maxcom / N)
                
            result["random failure"]=rf
        
        elif strategy == "標的型攻撃(degree)":
            dta = [1]
            while(G_ig.vcount() > 0):   
                betweenness=G_ig.degree()
                max_index = betweenness.index(max(betweenness))
                G_ig.delete_vertices(max_index)                
                maxcom=G_ig.components(mode="weak").giant()
                dta.append(maxcom.vcount()/N)
            
            result["degree"] =dta
        
        elif strategy == "標的型攻撃(closeness)":
            cta = [1]
            while(G_ig.vcount() > 0):
                
                betweenness=G_ig.closeness()
                max_index = betweenness.index(max(betweenness))
                G_ig.delete_vertices(max_index)      
                maxcom=G_ig.components(mode="weak").giant()
                cta.append(maxcom.vcount()/N)
            result["closeness"]=cta
        
        elif strategy == "標的型攻撃(betweenness)":
            bta = [1]
            while(G_ig.vcount() > 0):
                
                betweenness=G_ig.betweenness()
                max_index = betweenness.index(max(betweenness))
                G_ig.delete_vertices(max_index)                
                maxcom=G_ig.components(mode="weak").giant()
                bta.append(maxcom.vcount()/N)
     
            result["betweenness"]=bta
            
    return result

#ver.3
def ig_select_strategy2(G,strategy):
    G_ig = ig.Graph.from_networkx(G)
    N=G_ig.vcount()
    G_ig.vs["name"] = [str(v.index) for v in G_ig.vs]
    
    progress_placeholder = st.empty()
    progress_bar = progress_placeholder.progress(0)
    
    
    if strategy == "ランダム障害":
        N=nx.number_of_nodes(G)
        K=list(range(N))
        
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
        
        progress_placeholder.empty()    
        return rf
    
    if strategy == "標的型攻撃(degree)":
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
  
    