import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from module.network_models.models import models
from module.network_models.VIS_network import VIS_components,downloud_adjacency,VIS_hist

#モデル可視化

def random_network_page():
    
    code_R='nx.gnp_random_graph(N,p)'
    st.write("### _random network model（ギルバートのモデル）_")
    
    st.code('import networkx as nx',language='python')
    
    st.code(code_R,language='python')
    st.caption("N:ノード数　p:接続確率")
    st.write("ｐの値が１に近付くと（ほぼ）完全グラフが生成され、処理に非常に時間がかかるので注意。")
    G=None
    
    with st.container(border=True):

        col1, col2 = st.columns([1, 3])
        with col1:
            N_value = st.slider("N_value", 10, 100, 40,step=10,key='R_slider1')
            p_value = st.slider("p_value", 0.0, 1.0, 0.3,key='R_slider2')
            vis_par=st.checkbox('特徴量',key='random_vis_par')
            dig_hist=st.checkbox('次数分布',key='random_deg_hist')
            gene_random=st.button(label='生成',key='R',use_container_width=True)
                
        with col2:    
            if gene_random :

                N=int(N_value)
                p=float(p_value)
                G = nx.gnp_random_graph(N,p)

                pr1 = dict(nx.degree_centrality(G))
                pos1 =nx.kamada_kawai_layout(G)
                nx.draw_networkx_edges(G, pos1,edge_color='Gray')
                nx.draw_networkx_nodes(G, pos1,node_color=list(pr1.values()), cmap=plt.cm.Reds,node_size=120,edgecolors='Gray')

                plt.axis('off')
                plt.tight_layout()
                plt.suptitle(f"N={N} p={p} random_network_model")
                st.pyplot(plt)
                st.caption("次数が高いほどノードの色が濃く表現")
            
            
        if vis_par and gene_random:
            VIS_components.net_parameter(G)
        if dig_hist and gene_random:
            VIS_hist.visualization_hist(G)
    if G:                
        downloud_adjacency.downloud_adjacency_list_button(G)        
                       
def WS_model_page():
    code_WS='nx.watts_strogatz_graph(N,p)'
    st.write("### _watts-strogatz model（WSモデル）_")
    st.code('import networkx as nx',language='python')
    st.code(code_WS,language='python')
    st.caption("N:ノード数　p:再配線確率")
      
    col1, col2 = st.columns([1, 3])
    G=None
    with col1:
        
        N_value = st.slider("N_value", 10, 300, 40,step=10,key='WS_slider1')
        k_value = st.slider("K_value", 2, 10, 3,key='WS_slider3')
        p_value = st.slider("p_value", 0.0, 1.0, 0.3,key='WS_slider2')
        vis_par=st.checkbox('特徴量',key='WS_check')
        dig_hist=st.checkbox('次数分布',key='ws_deg_hist')
        gene_ws = st.button(label='生成',key='WS',use_container_width=True)
                    
    with col2:    
        if gene_ws:
            N=int(N_value)
            k=int(k_value)
            p=float(p_value)
            G = nx.watts_strogatz_graph(N,k,p)
            pr1 = dict(nx.degree_centrality(G))
            pos1 =nx.spring_layout(G, k=0.4)
            nx.draw_networkx_edges(G, pos1,edge_color='Gray')
            nx.draw_networkx_nodes(G, pos1,node_color=list(pr1.values()), cmap=plt.cm.Reds,node_size=120,edgecolors='Gray')
            
            plt.axis('off')
            plt.tight_layout()
            plt.suptitle(f"N={N} k={k} p={p} WS_model")
            st.pyplot(plt)
            st.caption("次数が高いほどノードの色が濃く表現")
            
    if vis_par and gene_ws:
        VIS_components.net_parameter(G)
    if dig_hist and gene_ws:
        VIS_hist.visualization_hist(G)
    if G:                
        downloud_adjacency.downloud_adjacency_list_button(G)                  
            
def BA_model_page():
    code_BA='nx.barabasi_albert_graph(N,m)'
    st.write("### _Barabasi-Albert model(BAモデル)_")
    st.code('import networkx as nx',language='python')    
    st.code(code_BA,language='python')
    st.caption("N:ノード数　m:新しいノードが接続されるリンク数")
    
        
    col1, col2 = st.columns([1, 3])
    G=None
    with col1:
        N_value = st.slider("N_value", 10, 300, 40,step=10,key='BA_slider1')
        m_value = st.slider("m_value", 1, 10, 3,key='BA_slider2')
        vis_par=st.checkbox('特徴量',key='BA_check')
        dig_hist=st.checkbox('次数分布',key='ba_deg_hist')
        gene_BA=st.button(label='生成',key='BA',use_container_width=True)
    with col2: 
        if gene_BA:
            N=int(N_value)
            m=int(m_value)
            G = nx.barabasi_albert_graph(N,m)
            pr1 = dict(nx.degree_centrality(G))
            pos1 =nx.kamada_kawai_layout(G)
            nx.draw_networkx_edges(G, pos1,edge_color='Gray')
            nx.draw_networkx_nodes(G, pos1,node_color=list(pr1.values()), cmap=plt.cm.Reds,node_size=120,edgecolors='Gray')
            plt.axis('off')
            plt.tight_layout()
            plt.suptitle(f"N={N} m={m} BA_model")
            st.pyplot(plt)
            st.caption("次数が高いほどノードの色が濃く表現")   
            
    if vis_par and gene_BA:
        VIS_components.net_parameter(G)
    if dig_hist and gene_BA:
        VIS_hist.visualization_hist(G)
    if G:                
        downloud_adjacency.downloud_adjacency_list_button(G)                   
    
def RW_page():
    st.write("""
             ### _ランダムウォークモデル_
             ライブラリになかったのでとりあえずナイーブな実装をしました。\n
             アルゴリズムは調整予定です。
             
             初期状態はN=4の完全グラフにしたけど諸説あり。
             """)
    
    code='''
    import networkx as nx
    import random as rd
    '''
    st.code(code,language='python')

    st.code('random_walk_graph(N,p)',language='python')
    st.caption("N:ノード数 　p:隣接ノードへの接続確率")
    code_RW='''
def random_walk_graph(N,m,p):
    G=nx.complete_graph(4)
    for i in range(4,N): 
        l=list(nx.nodes(G))
        j=rd.choice(l)
        G.add_edge(i,j)
        selected=set([i])
        for _ in range(m-1):
            random_value = rd.random() #確率ｐで隣接ノードに接続するかしないか場合分け。
            if random_value<p:
                unvisited_neighbors = [n for n in G.neighbors(j) if (n not in selected )]
                if not unvisited_neighbors:
                    break
                s=rd.choice(unvisited_neighbors)
                G.add_edge(i,s)
                selected.add(s)  
            else:
                unvisited_nodes = [n for n in G.nodes if (n not in selected)]
                if not unvisited_nodes:
                    break
                s=rd.choice(unvisited_nodes)
                G.add_edge(i,s)
                selected.add(s)
    return G
        '''  
    with st.expander("実装コード"):
        st.write("## _ランダムウォークモデル_")
        st.code(code_RW,language='python')            

    col1, col2 = st.columns([1, 3])
    G_RW=None
    with col1:
        N_RW_value = st.slider("N_value", 10, 300, 50,step=10,key='RW_slider1')
        m_RW_value = st.slider("m_value",1,10,3,key="RW_slider3")
        p_RW_value = st.slider("p_value", 0.0, 1.0, 0.5,key='RW_slider2')
        vis_par=st.checkbox('特徴量',key='rw')
        dig_hist=st.checkbox('次数分布',key='rw_deg_hist')
        gene_rw=st.button(label='生成',key=2,use_container_width=True)
    with col2:          
        if gene_rw:
            N=int(N_RW_value)
            m=int(m_RW_value)
            p=float(p_RW_value)
            G_RW = models.random_walk_graph(N,m,p)
            pr_RW = dict(nx.degree_centrality(G_RW))
            pos_RW =nx.spring_layout(G_RW, k=0.4) 
            nx.draw_networkx_edges(G_RW, pos_RW,edge_color='Gray')
            nx.draw_networkx_nodes(G_RW, pos_RW,node_color=list(pr_RW.values()), cmap=plt.cm.Reds,node_size=120,edgecolors='Gray')                 

            plt.axis('off')
            plt.tight_layout()
            plt.suptitle(f"N={N} p={p} random walk model")
            st.pyplot(plt)
            st.caption("次数が高いほどノードの色が濃く表現") 
            
    if vis_par and gene_rw:
        VIS_components.net_parameter(G_RW)
    if dig_hist and gene_rw:
        VIS_hist.visualization_hist(G_RW)
    if G_RW:                
        downloud_adjacency.downloud_adjacency_list_button(G_RW)   

def step_RW_page():
    st.write("""
             ### _ランダムウォークモデル(別ver)_
             ノード$j$から最大$l$ステップまでのランダムウォークを実行し、ノード$i$と接続する。
             """)

    code='''
    import networkx as nx
    import random as rd
    '''
    st.code(code,language="python")
    st.code('step_RW_graph(N,p,l)',language='python')
    st.caption("N:ノード数 　p:未訪問の隣接ノードへの接続確率　l:最大ウォーク数")
    code='''
    
    def step_RW_graph(N,p,l=None):
    
    #最大ステップ数を設定したい場合のみｌを入力
    
    if not l:
        l=N
    
    G=nx.complete_graph(4)　#初期状態N＝４の完全グラフ
    for i in range(4,N):  
        node_list=list(nx.nodes(G))　#Gのノードリストを取得。
        j=rd.choice(node_list)#ノードiを追加、ノードリストからランダムに一つノードｊを選択。
        G.add_edge(i,j) #リンクｉｊを生成。               
        random_value = rd.random() #乱数を生成。      
        if random_value<p:　#確率ｐで隣接ノードに接続するかしないか場合分け。
            current_node=j
            walk=[current_node]#ウォークを格納
            visited = set(walk)#到達済み判定
            for _ in range(l):
                if rd.random()<p:
                    unvisited_neighbors = [n for n in G.neighbors(current_node) if (n not in visited and n!=i)]
                    if unvisited_neighbors:
                        next_node = rd.choice(unvisited_neighbors)
                        walk.append(next_node)
                        visited.add(next_node)
                        current_node = next_node
                    else :   
                        break #移動先無しで終了
                else:
                    break #1-pで終了       
            for k in walk:
                G.add_edge(i,k)        
        else: 
            node_list.remove(j)
            s=rd.choice(node_list)
            G.add_edge(i,s)        
    return G    
    '''
    with st.expander("実装コード"):
        st.write("## _ランダムウォークモデル(ver.2)_")
        st.code(code,language="python")
        
    col1, col2 = st.columns([1, 3])
    G_RW=None
    with col1:
        N_value = st.slider("N_value", 10, 300, 50,step=10,key='SRW_slider1')
        p_value = st.slider("p_value", 0.0, 1.0, 0.5,key='SRW_slider2')
        vis_par=st.checkbox('特徴量',key='srw')
        dig_hist=st.checkbox('次数分布',key='sws_deg_hist')
        gene_srw = st.button(label='生成',key=2,use_container_width=True)
    with col2:          
        if gene_srw:
            N=int(N_value)
            p=float(p_value)

            G_RW = models.step_RW_graph(N,p)
            pr_RW = dict(nx.degree_centrality(G_RW))
            pos_RW =nx.spring_layout(G_RW, k=0.4) 
            nx.draw_networkx_edges(G_RW, pos_RW,edge_color='Gray')
            nx.draw_networkx_nodes(G_RW, pos_RW,node_color=list(pr_RW.values()), cmap=plt.cm.Reds,node_size=120,edgecolors='Gray')
                

            plt.axis('off')
            plt.tight_layout()
            plt.suptitle(f"N={N} m={p} step_random_walk")
            st.pyplot(plt)
            st.caption("次数が高いほどノードの色が濃く表現") 
            
    if vis_par and gene_srw:
        VIS_components.net_parameter(G_RW)
    if dig_hist and gene_srw:
        VIS_hist.visualization_hist(G_RW)
    if G_RW:                
        downloud_adjacency.downloud_adjacency_list_button(G_RW)             
    


