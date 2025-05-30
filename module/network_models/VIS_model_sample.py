import streamlit as st
import networkx as nx

from module.network_models.models import models
from module.network_models.VIS_network import downloud_adjacency,VIS_hist, net_parameter
from module.network_models.draw_plot import draw_plot_go

#モデル可視化

def random_network_page():
    
    code_R='nx.gnp_random_graph(N,p)'
    st.write("### _random network model（ギルバートのモデル）_")
    
    st.code('import networkx as nx',language='python')
    
    st.code(code_R,language='python')
    st.caption("N:ノード数　p:接続確率")
    st.write("ｐの値が１に近付くと（ほぼ）完全グラフが生成され、処理に非常に時間がかかるので注意。")
    G=None
    


    col1, col2 = st.columns([1, 3])
    
    with col1:
        with st.container(border=True):
            N_value = st.slider("N_value", 10, 500, 40,step=10,key='R_slider1')
            p_value = st.slider("p_value", 0.0, 1.0, 0.3,key='R_slider2')
            vis_par=st.checkbox('特徴量',key='random_vis_par')
            dig_hist=st.checkbox('次数分布',key='random_deg_hist')
            gene_random=st.button(label='生成',key='R',use_container_width=True)
            
    with col2:    
        if gene_random :
            N=int(N_value)
            p=float(p_value)
            G = nx.gnp_random_graph(N,p)

            fig=draw_plot_go(G)
            st.plotly_chart(fig, use_container_width=False)
            
    col3, col4 = st.columns([3, 5]) 
            
    with col3:
        if vis_par and gene_random:
            net_parameter.net_parameter(G)
    with col4:
        if dig_hist and gene_random:
            st.subheader("Degree distributions")
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
        with st.container(border=True):        
            N_value = st.slider("N_value", 10, 500, 40,step=10,key='WS_slider1')
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
            
            fig=draw_plot_go(G)
            st.plotly_chart(fig, use_container_width=False)
            
    col3, col4 = st.columns([3, 5]) 
            
    with col3:
        if vis_par and gene_ws:
            net_parameter.net_parameter(G)
    with col4:
        if dig_hist and gene_ws:
            st.subheader("Degree distributions")
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
        with st.container(border=True):
            N_value = st.slider("N_value", 10, 500, 40,step=10,key='BA_slider1')
            m_value = st.slider("m_value", 1, 10, 3,key='BA_slider2')
            vis_par=st.checkbox('特徴量',key='BA_check')
            dig_hist=st.checkbox('次数分布',key='ba_deg_hist')
            gene_BA=st.button(label='生成',key='BA',use_container_width=True)
    with col2: 
        if gene_BA:
            N=int(N_value)
            m=int(m_value)
            G = nx.barabasi_albert_graph(N,m)
            fig=draw_plot_go(G)
            st.plotly_chart(fig, use_container_width=False)
            
    col3, col4 = st.columns([3, 5]) 
            
    with col3:
        if vis_par and gene_BA:
            net_parameter.net_parameter(G)
    with col4:
        if dig_hist and gene_BA:
            st.subheader("Degree distributions")
            VIS_hist.visualization_hist(G)
    if G:                
        downloud_adjacency.downloud_adjacency_list_button(G)                    
    
def HK_model_page():
    st.write("""
             ### _Holme-Kim model_
             """)
    
    code='''
    import networkx as nx
    '''
    st.code(code,language='python')

    st.code('nx.powerlaw_cluster_graph(N, m, p)',language='python')
    st.caption("N:ノード数 　p:隣接ノードへの接続確率")
               
    col1, col2 = st.columns([1, 3])
    G_RW=None
    with col1:
        with st.container(border=True):
            N_RW_value = st.slider("N_value", 10, 500, 50,step=10,key='RW_slider1')
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
            G_RW = nx.powerlaw_cluster_graph(N, m, p)
            fig=draw_plot_go(G_RW)
            st.plotly_chart(fig, use_container_width=False)
            
    col3, col4 = st.columns([3, 5]) 
            
    with col3:
        if vis_par and gene_rw:
            net_parameter.net_parameter(G_RW)
    with col4:
        if dig_hist and gene_rw:
            st.subheader("Degree distributions")
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
        with st.container(border=True):
            N_value = st.slider("N_value", 10, 500, 50,step=10,key='SRW_slider1')
            p_value = st.slider("p_value", 0.0, 1.0, 0.5,key='SRW_slider2')
            vis_par=st.checkbox('特徴量',key='srw')
            dig_hist=st.checkbox('次数分布',key='sws_deg_hist')
            gene_srw = st.button(label='生成',key=2,use_container_width=True)
    with col2:          
        if gene_srw:
            N=int(N_value)
            p=float(p_value)

            G_RW = models.step_RW_graph(N,p)
            fig=draw_plot_go(G_RW)
            st.plotly_chart(fig, use_container_width=False) 
            
    col3, col4 = st.columns([3, 5]) 
            
    with col3:
        if vis_par and gene_srw:
            net_parameter.net_parameter(G_RW)
    with col4:
        if dig_hist and gene_srw:
            st.subheader("Degree distributions")
            VIS_hist.visualization_hist(G_RW)
    if G_RW:                
        downloud_adjacency.downloud_adjacency_list_button(G_RW)             
