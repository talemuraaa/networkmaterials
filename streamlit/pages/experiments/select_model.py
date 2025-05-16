import streamlit as st
import networkx as nx
from pages.network_models import models

def model_select(N,i):
    with st.container(height=310):
        col1,col2=st.columns([3,5],border=True)
        
        with col1:
            st.write(f"#### _Network{i}_")
            network=st.selectbox("モデルを選択",
                                 ("random network","watts-strogatz model","Barabasi-Albert model",
                                  "random walk","step random walk"),
                                 key=f'{i}mainbox')
        with col2:
            if network == "random network":
                button=st.checkbox("保存",key=f'{i}rd_button')               
                p_value = st.slider("p_value", 0.0, 1.0, 0.3,key=f'{i}rundom_slider')
                p=float(p_value)
                
                if button:
                    G=nx.gnp_random_graph(N,p)
                    return G
                
            if network == "watts-strogatz model":
                button=st.checkbox("保存",key=f'{i}ws_button')
                k_value = st.slider("K_value", 2, 50, 3,key=f'{i}WS_slider1')
                p_value = st.slider("m_value", 0.0, 1.0, 0.3,key=f'{i}WS_slider2')
                k=int(k_value)
                p=float(p_value)
                
                if button:
                    G=nx.watts_strogatz_graph(N,k,p)
                    return G                
                
                
            if network =="Barabasi-Albert model":
                button=st.checkbox("保存",key=f'{i}ba_button')
                m_value = st.slider("m_value", 1, 50, 3,key=f'{i}BA_slider2')
                m=int(m_value)
                
                if button:
                    G=nx.barabasi_albert_graph(N,m)
                    return G
                
            if network == "random walk":
                button=st.checkbox("保存",key=f'{i}rw_button')
                m_RW_value = st.slider("m_value",1,50,3,key=f'{i}RW_slider1')
                p_RW_value = st.slider("p_value", 0.0, 1.0, 0.5,key=f'{i}RW_slider2')
                m=int(m_RW_value)
                p=float(p_RW_value)
                
                if button:
                    G=models.random_walk_graph(N,m,p)
                    return G
                
                
                
            if network =="step random walk":
                button=st.checkbox("保存",key=f'{i}srw_button')
                p_value = st.slider("p_value", 0.0, 1.0, 0.5,key=f'{i}SRW_slider2')
                l_value = st.slider("l_value", 1,100,3,key=f'{i}SRW_slider3')
                p=float(p_value)
                l=int(l_value)
                
                if button:
                    G=models.step_RW_graph(N,p,l)
                    return G
                   