import streamlit as st
import networkx as nx
import pandas as pd
import plotly.io as pio
import io
from module.experiments_comp.draw_plot import draw_3Dplot_go,draw_2Dplot_go
from module.experiments_comp.select_model import model_select_ver3
from module.experiments_comp import net_parameter

def filterd_node(G,degree=0):
    filtered_nodes = [n for n in G.nodes() if G.degree(n) > degree]
    return  G.subgraph(filtered_nodes)


def main_VIS_network():
        
    st.header("ネットワークモデルの可視化及び解析(beta)",divider="violet")
    
    
    with st.container(height=400):
        col_3,col_4=st.columns([5,2])
        with col_3:
            G = model_select_ver3()

        with col_4:
            if G :
                net_parameter.net_parameter(G)
    
    col_another,col_vis=st.columns([1,1],border=True)
        
    with col_another:
        detill_list=st.multiselect("表示内容",["次数分布","特徴量","可視化","中心性"],default=["次数分布","特徴量","可視化"],key="detill")
        
    with col_vis:
        
        if "可視化" in detill_list:
            st.write("#### _plotly config_")
            
            dim=st.number_input("dim",min_value=2,max_value=3,key="dim_number")
            node_size=st.number_input("node_size",min_value=1,max_value=15,value=8)
            pos_select=st.selectbox("layout",('spring','kamada_kawai'),key="pos_select")    
            filter_degree = st.slider("次数フィルター", 0,10,key="filter")

            fig = None 
            
    
    #3Dオブジェクトを生成        
    if "可視化" in detill_list:
    
        if st.button(f"{dim}Dオブジェクトを生成",key="gene_3d"):
            with st.spinner("生成中"):
                
                
                
                if pos_select == 'spring':
                    full_pos = nx.spring_layout(G, dim=dim, iterations=10, scale=2.0, seed=42)
                else:
                    full_pos = nx.kamada_kawai_layout(G, dim=dim, scale=2.0)
            
                full_centrality = dict(nx.degree_centrality(G))
                H = filterd_node(G, filter_degree)
                fixed_pos_H = {n: full_pos[n] for n in H.nodes()}   
                
                draw_plot_dect={2:draw_2Dplot_go,3:draw_3Dplot_go}
                
                
                
                fig = draw_plot_dect.get(dim)(
                    H,
                    node_size=node_size,
                    layout_type=pos_select,
                    custom_pos=fixed_pos_H,
                    custom_centrality=full_centrality
                    )        
                fig.update_layout(height=800)
                st.plotly_chart(fig)
            
        if fig is not None:
            
            html_str = pio.to_html(fig, full_html=True, include_plotlyjs='cdn')
            st.download_button(label="HTML",
                data=html_str,
                file_name="3d_sample_graph.html",
                mime="text/html"
            )    
            
    