import networkx as nx 
import random as rd
import igraph as ig

from module.experiments_comp.attack_comp import attack_strategies

def select_single_strategy(networks:list,strategy)->dict:
    
    attack_function={
        "random failures": attack_strategies.random_failure,
        "targeted attack(degree)": attack_strategies.degree_traget_attack,
        "targeted attack(closeness)":attack_strategies.degree_traget_attack,
        "targeted attack(betweenness)":attack_strategies.betweenness_target_attack
            }
    
    result={}
    
    for i in range(len(networks)):
        result[i]=attack_function.get(strategy)(networks[i])
        
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
          

        if strategy == "random failures":
            result["random failure"]=attack_strategies.random_failure(G_copy)
        
        elif strategy == "targeted attack(degree)":
            result["degree"] =attack_strategies.degree_traget_attack(G_copy)
        
        elif strategy == "targeted attack(closeness)":                
            result["closeness"]= attack_strategies.closeness_traget_attack(G_copy)
        
        elif strategy == "targeted attack(betweenness)":
            result["betweenness"]=attack_strategies.betweenness_target_attack(G_copy)
    
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
