#標的型攻撃を再現
#ランダム障害を再現
#次数の生存関数と崩壊量の棒グラフを出力

n = 800 #ノード数

import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import numpy as np

f,axs = plt.subplots(1,2,width_ratios=[6,8],height_ratios=[7],figsize=(14,7))

#ネットワークを生成
#ノード数を取得
G = nx.watts_strogatz_graph(n,5,0.6)
G_copy1 =G.copy()
G_copy2 =G.copy()
G_copy3 =G.copy()
N = n

K = list(range(N))

#以下次数分布

degree_sequence=sorted(G.degree(),reverse=True)
kukan=range(0,max(degree_sequence,key=lambda x:x[1])[1]+2)
hist,kukan=np.histogram(degree_sequence,kukan,density=True)

axs[0].plot(hist)
axs[0].set_xlabel('degree')
axs[0].set_ylabel('frequency')
axs[0].grid(True)

#生存関数

def degree_target_arracks(G):
    dta =[]
    while(nx.number_of_nodes(G) > 0):
        d=dict(nx.degree_centrality(G))
        maxcom2=len(max(nx.connected_components(G),key=len,default=[0]))
        dta.append(maxcom2/N)
        G.remove_node(max(d,key=d.get))
    return dta



def closeness_target_attacks(G):
    cta = []
    while(nx.number_of_nodes(G) > 0):
        d=dict(nx.closeness_centrality(G))
        maxcom2=len(max(nx.connected_components(G),key=len,default=[0]))
        cta.append(maxcom2/N)
        G.remove_node(max(d,key=d.get))
        
    return cta

def betweenness_target_attacks(G):
    bta = []
    while(nx.number_of_nodes(G) > 0):
        d=dict(nx.betweenness_centrality(G))
        maxcom2=len(max(nx.connected_components(G),key=len,default=[0]))
        bta.append(maxcom2/N)
        G.remove_node(max(d,key=d.get))    
    
    return bta

def random_failures(G):
    
    K = list(range(nx.number_of_nodes(G)))
    samp = rd.sample(K,N)

    rf =[]
    i=0
    for i in samp:
        G.remove_node(i)
        maxcom=len(max(nx.connected_components(G),key=len,default=[0]))
        rf.append(maxcom/N)
    return rf

axs[1].plot(K,closeness_target_attacks(G),marker=".",markersize=5,label='c_target')
axs[1].plot(K,degree_target_arracks(G_copy1),marker=".",markersize=5,label='d_target')
axs[1].plot(K,betweenness_target_attacks(G_copy2),marker=".",markersize=5,label='b_target')
axs[1].plot(K,random_failures(G_copy3),marker=".",markersize=5,label='random')
axs[1].set_xlabel("Number of nodes removed")
axs[1].set_ylabel("Percentage of nodes in giant connected component")

plt.legend(loc='lower center', bbox_to_anchor=(.5, 1.01), ncol=3)
axs[1].grid(True)

f.savefig('network7_3_2.png')