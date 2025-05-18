import streamlit as st
import networkx as nx
from module.network_models import models

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
            if N==None:
                N=st.slider("N_value",0,3000,500,key=f'{i}Nslider')
            if network == "random network":
                              
                p_value = st.slider("p_value", 0.0, 1.0, 0.3,key=f'{i}rundom_slider')
                p=float(p_value)
                button=st.checkbox("check",key=f'{i}rd_button',label_visibility="collapsed") 
                if button:
                    G=nx.gnp_random_graph(N,p)
                    return G
                
            if network == "watts-strogatz model":
                
                k_value = st.slider("K_value", 2, 50, 3,key=f'{i}WS_slider1')
                p_value = st.slider("m_value", 0.0, 1.0, 0.3,key=f'{i}WS_slider2')
                k=int(k_value)
                p=float(p_value)
                button=st.checkbox("check",key=f'{i}ws_button',label_visibility="collapsed")
                if button:
                    G=nx.watts_strogatz_graph(N,k,p)
                    return G                
                
                
            if network =="Barabasi-Albert model":
                
                m_value = st.slider("m_value", 1, 50, 3,key=f'{i}BA_slider2')
                m=int(m_value)
                button=st.checkbox("check",key=f'{i}ba_button',label_visibility="collapsed")
                if button:
                    G=nx.barabasi_albert_graph(N,m)
                    return G
                
            if network == "random walk":
                
                m_RW_value = st.slider("m_value",1,50,3,key=f'{i}RW_slider1')
                p_RW_value = st.slider("p_value", 0.0, 1.0, 0.5,key=f'{i}RW_slider2')
                m=int(m_RW_value)
                p=float(p_RW_value)
                button=st.checkbox("check",key=f'{i}rw_button',label_visibility="collapsed")
                if button:
                    G=models.random_walk_graph(N,m,p)
                    return G
                
                
                
            if network =="step random walk":
                
                p_value = st.slider("p_value", 0.0, 1.0, 0.5,key=f'{i}SRW_slider2')
                l_value = st.slider("l_value", 1,100,3,key=f'{i}SRW_slider3')
                p=float(p_value)
                l=int(l_value)
                button=st.checkbox("check",key=f'{i}srw_button',label_visibility="collapsed")
                if button:
                    G=models.step_RW_graph(N,p,l)
                    return G
                   